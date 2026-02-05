from __future__ import annotations

import json
import threading
import time
from dataclasses import dataclass

from polyalphabot.models.entities import TgeSignal
from polyalphabot.services.tge_store import TgeRecord, TgeStore
from polyalphabot.services.clock import utc_now


@dataclass
class TgeDeduper:
    window_seconds: int
    store: TgeStore

    def __post_init__(self) -> None:
        self._lock = threading.Lock()
        self._seen: dict[tuple[str, str], float] = {}

    def seen(self, source: str, signal: TgeSignal) -> bool:
        key = (signal.token_symbol.lower(), signal.token_name.lower())
        now = time.time()
        with self._lock:
            self._prune(now)
            if key in self._seen:
                return True
            if not self._persist(source, signal):
                self._seen[key] = now
                return True
            self._seen[key] = now
            return False

    def _persist(self, source: str, signal: TgeSignal) -> bool:
        launch_time = signal.launch_time.isoformat() if signal.launch_time else None
        record = TgeRecord(
            source=source,
            token_symbol=signal.token_symbol,
            token_name=signal.token_name,
            launch_time=launch_time,
            received_at=utc_now().isoformat(),
            raw_json=json.dumps(signal.raw, ensure_ascii=False),
        )
        return self.store.insert_if_new(record)

    def _prune(self, now: float) -> None:
        stale = [k for k, ts in self._seen.items() if now - ts > self.window_seconds]
        for k in stale:
            self._seen.pop(k, None)
