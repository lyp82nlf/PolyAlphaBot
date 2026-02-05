from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor
from typing import List

from polyalphabot.core.engine import TradingEngine
from polyalphabot.models.entities import TgeSignal
from polyalphabot.services.notification import Notifier

logger = logging.getLogger(__name__)


class MarketConsumer:
    def __init__(self, engines: List[TradingEngine], max_workers: int, notifier: Notifier) -> None:
        self._engines = engines
        self._executor = ThreadPoolExecutor(max_workers=max_workers)
        self._notifier = notifier

    def submit(self, signal: TgeSignal) -> None:
        for engine in self._engines:
            future = self._executor.submit(engine.on_tge_signal, signal)
            future.add_done_callback(self._handle_done)

    def _handle_done(self, future) -> None:
        try:
            future.result()
        except Exception as exc:
            logger.exception("Market consumer error")
            self._notifier.send_markdown(
                "消费执行错误",
                f"**error**: <font color=\"warning\">{exc}</font>",
            )
