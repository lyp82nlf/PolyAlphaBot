from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass
from typing import Any, Dict, List
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class GammaConfig:
    base_url: str = "https://gamma-api.polymarket.com"
    timeout_seconds: int = 15
    retries: int = 2
    retry_backoff_seconds: float = 1.0
    headers: Dict[str, str] | None = None


class GammaClient:
    def __init__(self, config: GammaConfig) -> None:
        self._config = config

    def public_search(self, params: Dict[str, Any]) -> Dict[str, Any]:
        query = urlencode(params, doseq=True)
        url = f"{self._config.base_url}/public-search?{query}"
        headers = {"accept": "application/json"}
        if self._config.headers:
            headers.update(self._config.headers)
        request = Request(url, headers=headers)
        last_exc: Exception | None = None
        for attempt in range(self._config.retries + 1):
            start = time.monotonic()
            try:
                with urlopen(request, timeout=self._config.timeout_seconds) as response:
                    data = response.read().decode("utf-8")
                elapsed = time.monotonic() - start
                payload = json.loads(data)
                pagination = payload.get("pagination") or {}
                logger.info(
                    "Gamma public_search page=%s events=%s hasMore=%s totalResults=%s elapsed=%.2fs",
                    params.get("page"),
                    len(payload.get("events") or []),
                    pagination.get("hasMore"),
                    pagination.get("totalResults"),
                    elapsed,
                )
                return payload
            except (URLError, TimeoutError, OSError) as exc:
                last_exc = exc
                if attempt >= self._config.retries:
                    break
                delay = self._config.retry_backoff_seconds * (2**attempt)
                logger.warning(
                    "Gamma public_search failed attempt=%s/%s err=%s retry_in=%.1fs",
                    attempt + 1,
                    self._config.retries + 1,
                    exc,
                    delay,
                )
                time.sleep(delay)
            except Exception as exc:
                last_exc = exc
                break
        if last_exc:
            raise last_exc
        raise RuntimeError("Gamma public_search failed with unknown error")
