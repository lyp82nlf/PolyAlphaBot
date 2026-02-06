from __future__ import annotations

from typing import List

from polyalphabot.adapters.base import PredictionMarketAdapter
from polyalphabot.adapters.opinion import OpinionAdapter
from polyalphabot.adapters.polymarket import PolymarketAdapter
from polyalphabot.adapters.predict import PredictAdapter
from polyalphabot.config.schema import AdapterConfig
from polyalphabot.services.notification import Notifier


def build_adapters(
    configs: List[AdapterConfig],
    notifier: Notifier | None = None,
    proxies: dict[str, str] | None = None,
) -> List[PredictionMarketAdapter]:
    adapters: List[PredictionMarketAdapter] = []
    for cfg in configs:
        name = cfg.name.lower()
        if name == "polymarket":
            market_db_path = str(cfg.extra.get("market_db_path", "data/polymarket_markets.db"))
            clob_headers = cfg.extra.get("clob_headers")
            clob_timeout_seconds = int(cfg.extra.get("clob_timeout_seconds", 20))
            clob_batch_size = int(cfg.extra.get("clob_batch_size", 100))
            adapters.append(
                PolymarketAdapter(
                    api_key=cfg.api_key,
                    market_db_path=market_db_path,
                    clob_headers=clob_headers,
                    clob_timeout_seconds=clob_timeout_seconds,
                    clob_batch_size=clob_batch_size,
                    proxies=proxies,
                    notifier=notifier,
                )
            )
        elif name == "opinion":
            if cfg.extra.get("enabled", False) is not True:
                continue
            adapters.append(OpinionAdapter(api_key=cfg.api_key))
        elif name == "predict":
            if cfg.extra.get("enabled", False) is not True:
                continue
            adapters.append(PredictAdapter(api_key=cfg.api_key))
        else:
            raise ValueError(f"Unknown adapter: {cfg.name}")
    return adapters
