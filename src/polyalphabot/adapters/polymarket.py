from __future__ import annotations

import json
import logging
from datetime import timedelta
from typing import List, Optional

from polyalphabot.adapters.base import PredictionMarketAdapter
from polyalphabot.models.entities import (
    Market,
    Order,
    OrderRequest,
    OrderSide,
    OrderType,
    Position,
    Quote,
    Trade,
)
from polyalphabot.services.clock import utc_now
from polyalphabot.services.market_url import polymarket_event_url
from polyalphabot.services.notification import Notifier
from polyalphabot.services.polymarket_clob import ClobClient, ClobConfig
from polyalphabot.services.polymarket_market_store import PolymarketStore
from polyalphabot.strategies.tge_market_sweep import TgeSweepConfig
from polyalphabot.utils.timeparse import parse_datetime

logger = logging.getLogger(__name__)

class PolymarketAdapter(PredictionMarketAdapter):
    """Placeholder adapter. Implement using docs in /docs."""

    def __init__(
        self,
        api_key: str | None = None,
        market_db_path: str = "data/polymarket_markets.db",
        clob_headers: dict[str, str] | None = None,
        clob_timeout_seconds: int = 20,
        clob_batch_size: int = 100,
        proxies: dict[str, str] | None = None,
        notifier: Notifier | None = None,
    ) -> None:
        self._api_key = api_key
        self._store = PolymarketStore(market_db_path)
        self._clob = ClobClient(
            ClobConfig(
                headers=clob_headers,
                timeout_seconds=clob_timeout_seconds,
                proxies=proxies,
            )
        )
        self._clob_batch_size = clob_batch_size
        self._notifier = notifier
        self._pending_sells: dict[str, list[tuple[float, float, float]]] = {}

    def name(self) -> str:
        return "polymarket"

    def search_markets(self, query: str, limit: int = 50) -> List[Market]:
        records = self._store.search_markets(query, limit)
        return [self._record_to_market(r) for r in records]

    def get_market(self, market_id: str) -> Market:
        record = self._store.get_market(market_id)
        if not record:
            raise ValueError(f"Market not found: {market_id}")
        return self._record_to_market(record)

    def get_quote(self, market_id: str) -> Quote:
        raise NotImplementedError("Implement quote via CLOB market data.")

    def place_order(self, request: OrderRequest) -> Order:
        order = Order(
            id=f"sim-{int(utc_now().timestamp())}",
            market_id=request.market_id,
            side=request.side,
            quantity=request.quantity,
            price=request.price,
            order_type=request.order_type,
            status="filled",
            created_at=utc_now(),
        )
        self._notify_order(order)
        if order.side == OrderSide.BUY:
            self._simulate_sell(order)
        return order

    def cancel_order(self, order_id: str) -> None:
        raise NotImplementedError("Implement cancel via CLOB order endpoints.")

    def get_open_orders(self) -> List[Order]:
        return []

    def get_positions(self) -> List[Position]:
        return []

    def get_trades(self, market_id: Optional[str] = None) -> List[Trade]:
        raise NotImplementedError("Implement trades via Data API.")

    def build_orders_for_tge(self, signal, config: TgeSweepConfig | None) -> List[OrderRequest]:
        if config is None:
            return []
        markets = self._find_candidate_markets(signal, config)
        if not markets:
            self._notify_no_match(signal)
            return []
        logger.info(
            "Polymarket candidates for %s/%s: %s",
            signal.token_symbol,
            signal.token_name,
            len(markets),
        )
        token_map = self._extract_token_ids(markets)
        if not token_map:
            logger.info("Polymarket token map empty for %s/%s", signal.token_symbol, signal.token_name)
            return []
        logger.info("Polymarket token map size=%s", len(token_map))
        requests = [{"token_id": token_id, "side": "BUY"} for token_id in token_map]
        try:
            books = self._clob.get_books_batch(requests, batch_size=self._clob_batch_size)
        except Exception:
            return []
        scored = self._score_markets(token_map, books, config)
        if not scored:
            logger.info("Polymarket scored empty for %s/%s", signal.token_symbol, signal.token_name)
            return []
        logger.info("Polymarket scored markets=%s", len(scored))
        self._notify_match(signal, markets)
        scored.sort(key=lambda item: item[0], reverse=True)
        _, market, price, quantity = scored[0]
        self._pending_sells.setdefault(market.id, []).append((price, quantity, config.target_sell_price))
        return [
            OrderRequest(
                market_id=market.id,
                side=OrderSide.BUY,
                quantity=quantity,
                price=price,
                order_type=OrderType.MARKET,
            )
        ]

    def _record_to_market(self, record) -> Market:
        try:
            payload = json.loads(record.raw_json)
        except json.JSONDecodeError:
            payload = {}
        description = str(payload.get("description", "")) if payload else ""
        return Market(
            id=record.market_id,
            name=record.question,
            description=description,
            tags=[],
            base_token=payload.get("denominationToken"),
            quote_token=None,
            is_active=bool(record.active) and not bool(record.closed),
            event_datetime=parse_datetime(record.event_date),
            metadata={
                "clobTokenIds": payload.get("clobTokenIds"),
                "outcomes": payload.get("outcomes"),
            },
        )

    def _find_candidate_markets(self, signal, config: TgeSweepConfig) -> List[Market]:
        candidates: List[Market] = []
        queries = [signal.token_symbol, signal.token_name]
        for q in queries:
            if not q:
                continue
            candidates.extend(self.search_markets(q, limit=200))
        if not candidates:
            return []
        if not signal.launch_time:
            return candidates
        window_end = signal.launch_time + timedelta(days=config.match_window_days)
        filtered: List[Market] = []
        for market in candidates:
            if market.event_datetime is None:
                continue
            if signal.launch_time <= market.event_datetime <= window_end:
                filtered.append(market)
        return filtered

    def _extract_token_ids(self, markets: List[Market]) -> dict[str, Market]:
        token_map: dict[str, Market] = {}
        for market in markets:
            token_ids = market.metadata.get("clobTokenIds")
            outcomes = market.metadata.get("outcomes")
            if not token_ids:
                continue
            if isinstance(token_ids, str):
                try:
                    token_ids = json.loads(token_ids)
                except json.JSONDecodeError:
                    continue
            if not isinstance(token_ids, list):
                continue
            index = 0
            if isinstance(outcomes, str):
                try:
                    outcomes = json.loads(outcomes)
                except json.JSONDecodeError:
                    outcomes = None
            if isinstance(outcomes, list):
                for i, outcome in enumerate(outcomes):
                    if str(outcome).strip().lower() == "yes":
                        index = i
                        break
            if index >= len(token_ids):
                continue
            token_id = str(token_ids[index])
            token_map[token_id] = market
        return token_map

    def _score_markets(self, token_map: dict[str, Market], books: list[dict], config: TgeSweepConfig):
        scored = []
        for book in books:
            token_id = str(book.get("asset_id", ""))
            market = token_map.get(token_id)
            if not market:
                continue
            asks = book.get("asks") or []
            avg_price, quantity = self._avg_price_for_notional(asks, config.buy_notional_usd)
            if avg_price is None or quantity is None:
                continue
            if avg_price >= 0.98:
                continue
            if avg_price > config.buy_price_cap:
                continue
            roe = (config.target_sell_price - avg_price) / avg_price
            if roe < config.min_expected_roe:
                continue
            scored.append((roe, market, avg_price, quantity))
        return scored

    @staticmethod
    def _avg_price_for_notional(asks: list, notional: float):
        remaining = notional
        total_cost = 0.0
        total_qty = 0.0
        for level in asks:
            try:
                price = float(level.get("price"))
                size = float(level.get("size"))
            except (TypeError, ValueError):
                continue
            if price <= 0 or size <= 0:
                continue
            level_cost = price * size
            if level_cost <= remaining:
                total_cost += level_cost
                total_qty += size
                remaining -= level_cost
            else:
                partial_qty = remaining / price
                total_cost += remaining
                total_qty += partial_qty
                remaining = 0.0
                break
        if total_qty <= 0:
            return None, None
        avg_price = total_cost / total_qty
        return avg_price, total_qty

    def close(self) -> None:
        self._store.close()

    def _notify_order(self, order: Order) -> None:
        if not self._notifier:
            return
        record = self._store.get_market(order.market_id)
        title = "下单成功（Polymarket）"
        if not record:
            self._notifier.send_markdown(title, f"**market_id**: {order.market_id}")
            return
        event_slug = self._store.get_event_slug(record.event_id) or ""
        url = polymarket_event_url(event_slug) if event_slug else ""
        cost = "N/A" if order.price is None else f"{order.price * order.quantity:.4f}"
        avg_price = "N/A" if order.price is None else f"{order.price:.4f}"
        created = order.created_at.isoformat()
        def color(text: str, tone: str = "info") -> str:
            return f"<font color=\"{tone}\">{text}</font>"
        message = (
            f"[{record.question}]({url})\n"
            f"**数量**: {color(f'{order.quantity:.4f}')}\n"
            f"**均价**: {color(avg_price)}\n"
            f"**金额**: {color(cost, 'warning')}\n"
            f"**下单时间**: {color(created, 'comment')}"
        )
        self._notifier.send_markdown(title, message)

    def _simulate_sell(self, order: Order) -> None:
        if not self._notifier:
            return
        plans = self._pending_sells.get(order.market_id)
        if not plans:
            return
        buy_price, quantity, target_sell_price = plans.pop(0)
        if not plans:
            self._pending_sells.pop(order.market_id, None)
        record = self._store.get_market(order.market_id)
        title = "模拟卖出（Polymarket）"
        url = ""
        question = order.market_id
        if record:
            event_slug = self._store.get_event_slug(record.event_id) or ""
            url = polymarket_event_url(event_slug) if event_slug else ""
            question = record.question
        proceeds = target_sell_price * quantity
        def color(text: str, tone: str = "info") -> str:
            return f"<font color=\"{tone}\">{text}</font>"
        message = (
            f"[{question}]({url})\n"
            f"**数量**: {color(f'{quantity:.4f}')}\n"
            f"**卖出价**: {color(f'{target_sell_price:.4f}')}\n"
            f"**卖出金额**: {color(f'{proceeds:.4f}', 'warning')}"
        )
        self._notifier.send_markdown(title, message)
        profit = proceeds - (buy_price * quantity)
        profit_message = (
            f"[{question}]({url})\n"
            f"**买入金额**: {color(f'{(buy_price * quantity):.4f}')}\n"
            f"**卖出金额**: {color(f'{proceeds:.4f}')}\n"
            f"**利润**: {color(f'{profit:.4f} U', 'info' if profit >= 0 else 'warning')}"
        )
        self._notifier.send_markdown("模拟交易利润", profit_message)

    def _notify_no_match(self, signal) -> None:
        if not self._notifier:
            return
        launch = signal.launch_time.date().isoformat() if signal.launch_time else "unknown"
        def color(text: str, tone: str = "warning") -> str:
            return f"<font color=\"{tone}\">{text}</font>"
        self._notifier.send_markdown(
            "TGE未匹配到市场",
            (
                f"**Symbol**: {color(signal.token_symbol)}\n"
                f"**Name**: {color(signal.token_name)}\n"
                f"**Launch**: {color(launch)}"
            ),
        )

    def _notify_match(self, signal, markets: List[Market]) -> None:
        if not self._notifier:
            return
        lines: List[str] = []
        for market in markets:
            record = self._store.get_market(market.id)
            if not record:
                continue
            event_slug = self._store.get_event_slug(record.event_id) or ""
            url = polymarket_event_url(event_slug) if event_slug else ""
            lines.append(f"- [{record.question}]({url})")
        title = f"TGE匹配成功（{len(lines)}）"
        launch = signal.launch_time.date().isoformat() if signal.launch_time else "unknown"
        def color(text: str, tone: str = "info") -> str:
            return f"<font color=\"{tone}\">{text}</font>"
        header = (
            f"**Symbol**: {color(signal.token_symbol)}\n"
            f"**Name**: {color(signal.token_name)}\n"
            f"**Launch**: {color(launch)}\n"
            f"**Markets**:"
        )
        self._send_markdown_lines(title, header, lines)

    def _send_markdown_lines(self, title: str, header: str, lines: List[str]) -> None:
        max_body = 3500
        batches: List[str] = []
        current = [header]
        current_len = len(header) + 1
        for line in lines:
            line_len = len(line) + 1
            if current and current_len + line_len > max_body:
                batches.append("\n".join(current))
                current = [header]
                current_len = len(header) + 1
            current.append(line)
            current_len += line_len
        if current:
            batches.append("\n".join(current))

        total = len(batches)
        for idx, body in enumerate(batches, start=1):
            batch_title = title if total == 1 else f"{title}（{idx}/{total}）"
            self._notifier.send_markdown(batch_title, body)
