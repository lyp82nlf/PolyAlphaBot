from __future__ import annotations

import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from queue import Queue
from typing import Iterable

from polyalphabot.models.entities import TgeSignal
from polyalphabot.services.tge_deduper import TgeDeduper
from polyalphabot.services.notification import Notifier
from polyalphabot.services.tge_source import TgeSource
from polyalphabot.services.clock import utc_now


@dataclass(frozen=True)
class TgeEnvelope:
    source: str
    signal: TgeSignal
    received_at: datetime


class TgeProducer(threading.Thread):
    def __init__(
        self,
        source: TgeSource,
        out_queue: Queue[TgeEnvelope],
        poll_interval_seconds: float,
        notifier: Notifier,
        error_threshold: int,
        error_window_seconds: int,
        deduper: TgeDeduper,
    ) -> None:
        super().__init__(daemon=True)
        self._source = source
        self._queue = out_queue
        self._poll_interval_seconds = poll_interval_seconds
        self._notifier = notifier
        self._error_threshold = error_threshold
        self._error_window_seconds = error_window_seconds
        self._deduper = deduper
        self._error_times: list[float] = []

    def run(self) -> None:
        while True:
            try:
                for signal in self._source.poll():
                    if self._is_past_launch(signal):
                        continue
                    if self._deduper.seen(self._source.name(), signal):
                        continue
                    self._notifier.send_markdown(
                        "新TGE事件",
                        self._format_tge_markdown(signal),
                    )
                    self._queue.put(
                        TgeEnvelope(
                            source=self._source.name(),
                            signal=signal,
                            received_at=datetime.now(timezone.utc),
                        )
                    )
            except Exception as exc:
                now = time.time()
                self._error_times.append(now)
                self._error_times = [t for t in self._error_times if now - t <= self._error_window_seconds]
                if len(self._error_times) >= self._error_threshold:
                    self._notifier.send_markdown(
                        "TGE轮询错误",
                        (
                            f"**source**: {self._source.name()}\n"
                            f"**errors**: {len(self._error_times)}\n"
                            f"**window**: {self._error_window_seconds}s\n"
                            f"**last**: {exc}"
                        ),
                    )
                    self._error_times.clear()
            time.sleep(self._poll_interval_seconds)

    @staticmethod
    def _format_tge_markdown(signal: TgeSignal) -> str:
        launch = signal.launch_time.date().isoformat() if signal.launch_time else "unknown"
        chain = signal.chain or "unknown"
        def color(text: str, tone: str = "info") -> str:
            return f"<font color=\"{tone}\">{text}</font>"
        return (
            f"**Symbol**: {color(signal.token_symbol)}\n"
            f"**Name**: {color(signal.token_name)}\n"
            f"**Chain**: {color(chain, 'comment' if chain == 'unknown' else 'info')}\n"
            f"**Launch**: {color(launch, 'warning' if launch == 'unknown' else 'info')}"
        )

    @staticmethod
    def _is_past_launch(signal: TgeSignal) -> bool:
        if not signal.launch_time:
            return False
        now = utc_now()
        launch = signal.launch_time
        if launch.tzinfo is None:
            launch = launch.replace(tzinfo=timezone.utc)
        return launch < now
