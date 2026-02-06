from __future__ import annotations

import logging
import os
from typing import Dict, Optional
from urllib.request import ProxyHandler, build_opener, urlopen

logger = logging.getLogger(__name__)


def resolve_proxies(
    http_proxy: Optional[str] = None,
    https_proxy: Optional[str] = None,
    all_proxy: Optional[str] = None,
) -> Optional[Dict[str, str]]:
    def getenv(key: str) -> Optional[str]:
        return os.environ.get(key) or os.environ.get(key.lower())

    http_value = http_proxy or getenv("HTTP_PROXY")
    https_value = https_proxy or getenv("HTTPS_PROXY")
    all_value = all_proxy or getenv("ALL_PROXY")

    proxies: Dict[str, str] = {}
    if http_value:
        proxies["http"] = http_value
    if https_value:
        proxies["https"] = https_value
    if not proxies and all_value:
        proxies["http"] = all_value
        proxies["https"] = all_value
        if all_value.startswith("socks"):
            logger.warning(
                "ALL_PROXY uses socks; urllib may not support this without PySocks: %s",
                all_value,
            )
    return proxies or None


def urlopen_with_proxy(request, timeout: int, proxies: Optional[Dict[str, str]] = None):
    if proxies is None:
        return urlopen(request, timeout=timeout)
    opener = build_opener(ProxyHandler(proxies))
    return opener.open(request, timeout=timeout)
