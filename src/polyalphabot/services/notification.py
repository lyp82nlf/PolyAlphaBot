from __future__ import annotations

import json
import logging
import threading
import time
from dataclasses import dataclass
from typing import Optional
from urllib.request import Request

from polyalphabot.utils.http import urlopen_with_proxy

logger = logging.getLogger(__name__)


class Notifier:
    def send(self, title: str, message: str) -> None:
        raise NotImplementedError

    def send_markdown(self, title: str, message: str) -> None:
        raise NotImplementedError


@dataclass(frozen=True)
class WeComConfig:
    webhook_url: Optional[str] = None
    timeout_seconds: int = 10
    cooldown_seconds: int = 60
    proxies: dict[str, str] | None = None


class WeComNotifier(Notifier):
    def __init__(self, config: WeComConfig) -> None:
        self._config = config
        self._lock = threading.Lock()
        self._last_sent: dict[str, float] = {}

    def send(self, title: str, message: str) -> bool:
        if not self._config.webhook_url:
            return False
        if self._should_throttle(title, message):
            return False
        payload = {
            "msgtype": "text",
            "text": {"content": f"{title}\n{message}"},
        }
        return self._post(payload)

    def send_markdown(self, title: str, message: str) -> bool:
        if not self._config.webhook_url:
            return False
        if self._should_throttle(title, message):
            return False
        payload = {
            "msgtype": "markdown",
            "markdown": {"content": f"**{title}**\n{message}"},
        }
        return self._post(payload)

    def _post(self, payload: dict) -> bool:
        data = json.dumps(payload).encode("utf-8")
        request = Request(
            self._config.webhook_url,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen_with_proxy(
                request,
                timeout=self._config.timeout_seconds,
                proxies=self._config.proxies,
            ) as response:
                body = response.read().decode("utf-8", errors="ignore")
            if body:
                try:
                    parsed = json.loads(body)
                    errcode = parsed.get("errcode")
                    if errcode not in (0, None):
                        logger.error("WeCom send error: %s", body)
                        return False
                except json.JSONDecodeError:
                    logger.info("WeCom response: %s", body)
            return True
        except Exception:
            logger.exception("WeCom send failed")
        return False

    def _should_throttle(self, title: str, message: str) -> bool:
        key = f"{title}|{message}"
        now = time.time()
        with self._lock:
            last = self._last_sent.get(key)
            if last is not None and now - last < self._config.cooldown_seconds:
                return True
            self._last_sent[key] = now
        return False
