from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Iterable, List, Optional
from urllib.request import Request, urlopen

from polyalphabot.models.entities import TgeSignal
from polyalphabot.services.tge_source import TgeSource

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class Alpha123Config:
    url: str = "https://alpha123.uk/api/data?fresh=1"
    headers: Dict[str, str] = None
    timeout_seconds: int = 10
    timezone_name: str = "UTC"


class Alpha123Source(TgeSource):
    def __init__(self, config: Alpha123Config) -> None:
        self._config = config

    def name(self) -> str:
        return "alpha123"

    def poll(self) -> Iterable[TgeSignal]:
        payload = self._fetch()
        airdrops = payload.get("airdrops", [])
        logger.info("alpha123 fetched airdrops=%s", len(airdrops))
        signals: List[TgeSignal] = []
        skipped_type = 0
        skipped_pretge = 0
        for item in airdrops:
            item_type = str(item.get("type", "")).lower()
            if item_type != "tge":
                skipped_type += 1
                continue
            if bool(item.get("pretge", False)):
                skipped_pretge += 1
                continue
            signal = self._to_signal(item)
            if signal is None:
                continue
            signals.append(signal)
        logger.info(
            "alpha123 signals=%s skipped_type=%s skipped_pretge=%s",
            len(signals),
            skipped_type,
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
        item_type = str(item.get("type", "")).lower()
        if item_type != "tge":
            return None
        if bool(item.get("pretge", False)):
            return None

        token_symbol = str(item.get("token", "")).strip()
        token_name = str(item.get("name", "")).strip()
        chain = str(item.get("chain_id", "")).strip() or None

        launch_time = self._parse_datetime(item)
        confidence = 0.8
        return TgeSignal(
            token_symbol=token_symbol,
            token_name=token_name,
            chain=chain,
            launch_time=launch_time,
            confidence=confidence,
            raw=item,
        )

    def _parse_datetime(self, item: Dict[str, object]) -> Optional[datetime]:
        date_str = str(item.get("date", "")).strip()
        time_str = str(item.get("time", "")).strip()
        utc_str = str(item.get("utc", "")).strip()

        if utc_str:
            try:
                return datetime.fromisoformat(utc_str.replace("Z", "+00:00"))
            except ValueError:
                pass

        if not date_str:
            return None

        if not time_str:
            time_str = "00:00"

        try:
            dt = datetime.fromisoformat(f"{date_str} {time_str}")
        except ValueError:
            return None

        if self._config.timezone_name.upper() == "UTC":
            return dt.replace(tzinfo=timezone.utc)
        return dt
