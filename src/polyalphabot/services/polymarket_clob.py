from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass
from typing import Any, Dict, List
from urllib.request import Request

from polyalphabot.utils.http import urlopen_with_proxy
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ClobConfig:
    base_url: str = "https://clob.polymarket.com"
    timeout_seconds: int = 20
    headers: Dict[str, str] | None = None
    proxies: Dict[str, str] | None = None


class ClobClient:
    def __init__(self, config: ClobConfig) -> None:
        self._config = config

    def get_books(self, requests: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        url = f"{self._config.base_url}/books"
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        if self._config.headers:
            headers.update(self._config.headers)
        data = json.dumps(requests).encode("utf-8")
        request = Request(url, data=data, headers=headers, method="POST")
        start = time.time()
        with urlopen_with_proxy(
            request,
            timeout=self._config.timeout_seconds,
            proxies=self._config.proxies,
        ) as response:
            payload = response.read().decode("utf-8")
        elapsed = time.time() - start
        logger.info("CLOB /books batch=%s bytes=%s elapsed=%.2fs", len(requests), len(data), elapsed)
        return json.loads(payload)

    def get_books_batch(self, requests: List[Dict[str, Any]], batch_size: int = 100) -> List[Dict[str, Any]]:
        results: List[Dict[str, Any]] = []
        if batch_size <= 0:
            batch_size = 100
        logger.info("CLOB batch request total=%s batch_size=%s", len(requests), batch_size)
        for i in range(0, len(requests), batch_size):
            batch = requests[i : i + batch_size]
            results.extend(self.get_books(batch))
        return results
