from __future__ import annotations

from typing import Dict, List

from polyalphabot.services.alpha123_source import Alpha123Config, Alpha123Source
from polyalphabot.services.alpha520_source import Alpha520Config, Alpha520Source
from polyalphabot.services.tge_source import TgeSource


def build_sources(configs: List[Dict[str, object]]) -> List[TgeSource]:
    sources: List[TgeSource] = []
    for cfg in configs:
        name = str(cfg.get("name", "")).lower()
        if name == "alpha123":
            headers = cfg.get("headers") or {}
            raw_url = cfg.get("url")
            url = str(raw_url).strip() if raw_url is not None else ""
            if not url or url.lower() in {"none", "null"}:
                url = "https://alpha123.uk/api/data?fresh=1"
            source = Alpha123Source(
                Alpha123Config(
                    url=url,
                    headers={str(k): str(v) for k, v in headers.items()},
                    timeout_seconds=int(cfg.get("timeout_seconds", 10)),
                    timezone_name=str(cfg.get("timezone_name", "UTC")),
                )
            )
            sources.append(source)
        elif name == "alpha520":
            headers = cfg.get("headers") or {}
            raw_url = cfg.get("url")
            url = str(raw_url).strip() if raw_url is not None else ""
            if not url or url.lower() in {"none", "null"}:
                url = "https://alpha520.com/api/airdrops/history"
            source = Alpha520Source(
                Alpha520Config(
                    url=url,
                    headers={str(k): str(v) for k, v in headers.items()},
                    timeout_seconds=int(cfg.get("timeout_seconds", 10)),
                )
            )
            sources.append(source)
        else:
            raise ValueError(f"Unknown TGE source: {name}")
    return sources
