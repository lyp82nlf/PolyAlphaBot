from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from polyalphabot.core.engine import EngineConfig
from polyalphabot.core.risk import RiskConfig
from polyalphabot.strategies.tge_market_sweep import TgeSweepConfig


@dataclass(frozen=True)
class AdapterConfig:
    name: str = "polymarket"
    api_key: Optional[str] = None
    extra: Dict[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class Settings:
    adapter: AdapterConfig = AdapterConfig()
    adapters: List[AdapterConfig] = field(default_factory=list)
    engine: EngineConfig = EngineConfig()
    risk: RiskConfig = RiskConfig()
    strategy: TgeSweepConfig = TgeSweepConfig()
    tge_sources: List[Dict[str, object]] = field(default_factory=list)
    poll_interval_seconds: float = 1.0
    error_threshold: int = 5
    error_window_seconds: int = 30
    wecom_webhook_url: Optional[str] = None
    wecom_cooldown_seconds: int = 60
    dedup_window_seconds: int = 3600
    consumer_max_workers: int = 4
    market_poll_interval_seconds: int = 60
    market_db_path: str = "data/polymarket_markets.db"
    gamma_headers: Dict[str, str] = field(default_factory=dict)
    tge_db_path: str = "data/tge_events.db"
    log_path: str = "logs/polyalphabot.log"
