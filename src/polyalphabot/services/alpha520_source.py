from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Iterable, List, Optional
from urllib.request import Request, urlopen

from polyalphabot.models.entities import TgeSignal
from polyalphabot.services.tge_source import TgeSource

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class Alpha520Config:
    url: str = "https://alpha520.com/api/airdrops/history"
    headers: Dict[str, str] = None
    timeout_seconds: int = 10


class Alpha520Source(TgeSource):
    def __init__(self, config: Alpha520Config) -> None:
        self._config = config

    def name(self) -> str:
        return "alpha520"

    def poll(self) -> Iterable[TgeSignal]:
        payload = self._fetch()
        items = payload.get("data", [])
        logger.info("alpha520 fetched items=%s", len(items))
        signals: List[TgeSignal] = []
        skipped_exact = 0
        skipped_pretge = 0
        for item in items:
            if bool(item.get("isExactTime", False)):
                skipped_exact += 1
                continue
            if bool(item.get("isPreTge", False)):
                skipped_pretge += 1
                continue
            signal = self._to_signal(item)
            if signal is None:
                continue
            signals.append(signal)
        logger.info(
            "alpha520 signals=%s skipped_exact=%s skipped_pretge=%s",
            len(signals),
            skipped_exact,
            skipped_pretge,
        )
        return signals

    def _fetch(self) -> Dict[str, object]:
        headers = self._config.headers or {}
        request = Request(self._config.url, headers=headers)
        with urlopen(request, timeout=self._config.timeout_seconds) as response:
            data = response.read().decode("utf-8")
        return json.loads(data)

    def _to_signal(self, item: Dict[str, object]) -> Optional[TgeSignal]:
        if bool(item.get("isExactTime", False)):
            return None
        if bool(item.get("isPreTge", False)):
            return None

        token_symbol = str(item.get("symbol", "")).strip()
        token_name = str(item.get("name", "")).strip()

        launch_time = self._parse_datetime(item.get("date"))
        confidence = 0.75
        return TgeSignal(
            token_symbol=token_symbol,
            token_name=token_name,
            chain=None,
            launch_time=launch_time,
            confidence=confidence,
            raw=item,
        )

    @staticmethod
    def _parse_datetime(value: object) -> Optional[datetime]:
        if not value:
            return None
        text = str(value)
        try:
            return datetime.fromisoformat(text.replace("Z", "+00:00"))
        except ValueError:
            return None
