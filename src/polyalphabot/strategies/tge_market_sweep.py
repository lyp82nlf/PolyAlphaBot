from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Optional

from polyalphabot.models.entities import Market, OrderRequest, OrderSide, OrderType, Quote, TgeSignal
from polyalphabot.strategies.base import Strategy


@dataclass(frozen=True)
class TgeSweepConfig:
    min_confidence: float = 0.7
    max_candidates: int = 10
    buy_price_cap: float = 0.9
    target_sell_price: float = 0.99
    min_expected_roe: float = 0.05
    order_quantity: float = 100.0
    buy_notional_usd: float = 100.0
    match_window_days: int = 6
    market_name_patterns: List[str] = None

    def normalized_patterns(self) -> List[re.Pattern[str]]:
        patterns = self.market_name_patterns or [
            r"will .* launch a token",
            r"will .* issue a token",
            r"will .* tge",
        ]
        return [re.compile(p, re.IGNORECASE) for p in patterns]


class TgeMarketSweepStrategy(Strategy):
    def __init__(self, config: TgeSweepConfig) -> None:
        self.config = config

    def name(self) -> str:
        return "tge_market_sweep"

    def _matches_market(self, market: Market) -> bool:
        haystack = f"{market.name} {market.description}".lower()
        for pattern in self.config.normalized_patterns():
            if pattern.search(haystack):
                return True
        return False

    def _expected_roe(self, buy_price: float) -> float:
        return (self.config.target_sell_price - buy_price) / buy_price

    def generate_orders(
        self,
        signal: TgeSignal,
        markets: List[Market],
        quotes: List[Quote],
    ) -> List[OrderRequest]:
        if signal.confidence < self.config.min_confidence:
            return []

        candidates = []
        quote_map = {q.market_id: q for q in quotes}
        for market in markets:
            if not self._matches_market(market):
                continue
            quote = quote_map.get(market.id)
            if not quote or quote.best_ask is None:
                continue
            buy_price = quote.best_ask
            if buy_price > self.config.buy_price_cap:
                continue
            roe = self._expected_roe(buy_price)
            if roe < self.config.min_expected_roe:
                continue
            candidates.append((roe, market, buy_price))

        candidates.sort(key=lambda item: item[0], reverse=True)
        orders: List[OrderRequest] = []
        for roe, market, buy_price in candidates[: self.config.max_candidates]:
            orders.append(
                OrderRequest(
                    market_id=market.id,
                    side=OrderSide.BUY,
                    quantity=self.config.order_quantity,
                    price=buy_price,
                    order_type=OrderType.LIMIT,
                )
            )
        return orders
