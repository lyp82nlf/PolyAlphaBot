from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List
from urllib.parse import urlencode
from urllib.request import Request, urlopen


@dataclass(frozen=True)
class GammaConfig:
    base_url: str = "https://gamma-api.polymarket.com"
    timeout_seconds: int = 15
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
        with urlopen(request, timeout=self._config.timeout_seconds) as response:
            data = response.read().decode("utf-8")
        return json.loads(data)
