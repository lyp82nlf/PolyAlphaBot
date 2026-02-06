from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict

from polyalphabot.config.schema import AdapterConfig, Settings
from polyalphabot.core.engine import EngineConfig
from polyalphabot.core.risk import RiskConfig
from polyalphabot.strategies.tge_market_sweep import TgeSweepConfig


class SettingsLoader:
    @staticmethod
    def load(path: str | Path) -> Settings:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        webhook = data.get("wecom_webhook_url")
        if webhook is not None and str(webhook).strip().lower() in {"none", "null"}:
            webhook = None
        return Settings(
            adapter=AdapterConfig(**data.get("adapter", {})),
            adapters=[AdapterConfig(**cfg) for cfg in data.get("adapters", [])],
            engine=EngineConfig(**data.get("engine", {})),
            risk=RiskConfig(**data.get("risk", {})),
            strategy=TgeSweepConfig(**data.get("strategy", {})),
            tge_sources=list(data.get("tge_sources", [])),
            poll_interval_seconds=float(data.get("poll_interval_seconds", 1.0)),
            error_threshold=int(data.get("error_threshold", 5)),
            error_window_seconds=int(data.get("error_window_seconds", 30)),
            wecom_webhook_url=webhook,
            wecom_cooldown_seconds=int(data.get("wecom_cooldown_seconds", 60)),
            dedup_window_seconds=int(data.get("dedup_window_seconds", 3600)),
            consumer_max_workers=int(data.get("consumer_max_workers", 4)),
            market_poll_interval_seconds=int(data.get("market_poll_interval_seconds", 60)),
            market_error_threshold=int(data.get("market_error_threshold", 3)),
            market_error_window_seconds=int(data.get("market_error_window_seconds", 300)),
            market_error_cooldown_seconds=int(data.get("market_error_cooldown_seconds", 600)),
            http_proxy=data.get("http_proxy"),
            https_proxy=data.get("https_proxy"),
            all_proxy=data.get("all_proxy"),
            market_db_path=str(data.get("market_db_path", "data/polymarket_markets.db")),
            gamma_headers={str(k): str(v) for k, v in (data.get("gamma_headers", {}) or {}).items()},
            gamma_timeout_seconds=int(data.get("gamma_timeout_seconds", 15)),
            gamma_retries=int(data.get("gamma_retries", 2)),
            gamma_retry_backoff_seconds=float(data.get("gamma_retry_backoff_seconds", 1.0)),
            tge_db_path=str(data.get("tge_db_path", "data/tge_events.db")),
            log_path=str(data.get("log_path", "logs/polyalphabot.log")),
        )

    @staticmethod
    def dump(path: str | Path, settings: Settings) -> None:
        payload: Dict[str, Any] = asdict(settings)
        Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")
