from __future__ import annotations

import json
import threading
import time
from dataclasses import dataclass
from typing import Dict, Iterable, List

from polyalphabot.services.notification import Notifier
from polyalphabot.services.polymarket_gamma import GammaClient
from polyalphabot.services.polymarket_market_store import EventRecord, MarketRecord, PolymarketStore
from polyalphabot.utils.timeparse import parse_datetime


@dataclass(frozen=True)
class MarketWatcherConfig:
    poll_interval_seconds: int = 60
    query: str = "launch a token"
    limit_per_type: int = 100
    keep_closed_markets: int = 1
    events_status: str | None = None


class PolymarketMarketWatcher(threading.Thread):
    def __init__(
        self,
        gamma: GammaClient,
        store: PolymarketStore,
        notifier: Notifier,
        config: MarketWatcherConfig,
    ) -> None:
        super().__init__(daemon=True)
        self._gamma = gamma
        self._store = store
        self._notifier = notifier
        self._config = config

    def run(self) -> None:
        while True:
            try:
                self._poll_once()
            except Exception as exc:
                self._notifier.send_markdown(
                    "市场同步错误",
                    f"**error**: <font color=\"warning\">{exc}</font>",
                )
            time.sleep(self._config.poll_interval_seconds)

    def _poll_once(self) -> None:
        events, markets = self._fetch_all()
        new_events = self._store.upsert_events(events)
        self._store.upsert_markets(markets)
        if not new_events:
            return
        self._notify_new_events(new_events)

    def _notify_new_events(self, new_events: List[EventRecord]) -> None:
        lines: List[str] = []
        for event in new_events:
            url = f"https://polymarket.com/event/{event.slug}"
            lines.append(f"- [{event.title}]({url})")
        self._send_markdown_batches(f"新市场事件（{len(new_events)}）", lines)

    def _send_markdown_batches(self, title: str, lines: List[str]) -> None:
        max_body = 3500
        batches: List[str] = []
        current: List[str] = []
        current_len = 0
        for line in lines:
            line_len = len(line) + 1
            if current and current_len + line_len > max_body:
                batches.append("\n".join(current))
                current = []
                current_len = 0
            current.append(line)
            current_len += line_len
        if current:
            batches.append("\n".join(current))

        total = len(batches)
        for idx, body in enumerate(batches, start=1):
            batch_title = title if total == 1 else f"{title}（{idx}/{total}）"
            self._notifier.send_markdown(batch_title, body)

    def _fetch_all(self) -> tuple[List[EventRecord], List[MarketRecord]]:
        page = 1
        events: List[EventRecord] = []
        markets: List[MarketRecord] = []

        while True:
            params: Dict[str, object] = {
                "q": self._config.query,
                "page": page,
                "limit_per_type": self._config.limit_per_type,
                "keep_closed_markets": self._config.keep_closed_markets,
                "cache": False,
                "search_profiles": False,
                "search_tags": False,
            }
            if self._config.events_status:
                params["events_status"] = self._config.events_status

            payload = self._gamma.public_search(params)
            page_events = payload.get("events") or []
            if not page_events:
                break

            for event in page_events:
                event_id = str(event.get("id", ""))
                title = str(event.get("title", ""))
                slug = str(event.get("slug", ""))
                created_at = event.get("createdAt")
                updated_at = event.get("updatedAt")
                event_date = event.get("eventDate") or event.get("startDate") or event.get("endDate")
                events.append(
                    EventRecord(
                        event_id=event_id,
                        title=title,
                        slug=slug,
                        created_at=created_at,
                        updated_at=updated_at,
                        event_date=event_date,
                        raw_json=json.dumps(event, ensure_ascii=False),
                    )
                )

                for market in event.get("markets", []) or []:
                    market_id = str(market.get("id", ""))
                    question = str(market.get("question", ""))
                    m_slug = str(market.get("slug", ""))
                    active = bool(market.get("active", False))
                    closed = bool(market.get("closed", False))
                    markets.append(
                        MarketRecord(
                            market_id=market_id,
                            event_id=event_id,
                            question=question,
                            slug=m_slug,
                            active=active,
                            closed=closed,
                            event_date=event_date,
                            raw_json=json.dumps(market, ensure_ascii=False),
                        )
                    )

            pagination = payload.get("pagination") or {}
            has_more = bool(pagination.get("hasMore", False))
            if not has_more:
                break
            page += 1

        return events, markets
