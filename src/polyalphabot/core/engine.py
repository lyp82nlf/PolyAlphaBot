from __future__ import annotations

from dataclasses import dataclass
import logging
from typing import List

from polyalphabot.adapters.base import PredictionMarketAdapter
from polyalphabot.core.risk import RiskConfig, RiskManager
from polyalphabot.execution.executor import Executor
from polyalphabot.models.entities import OrderRequest, TgeSignal
from polyalphabot.strategies.base import Strategy


@dataclass(frozen=True)
class EngineConfig:
    search_query: str = "token"
    search_limit: int = 100


class TradingEngine:
    def __init__(
        self,
        adapter: PredictionMarketAdapter,
        strategy: Strategy,
        risk_manager: RiskManager,
        executor: Executor,
        config: EngineConfig,
    ) -> None:
        self._adapter = adapter
        self._strategy = strategy
        self._risk = risk_manager
        self._executor = executor
        self._config = config

    def on_tge_signal(self, signal: TgeSignal) -> List[OrderRequest]:
        logger = logging.getLogger(__name__)
        logger.info("Engine %s handling TGE %s/%s", self._adapter.name(), signal.token_symbol, signal.token_name)
        orders: List[OrderRequest] = []
        build_orders = getattr(self._adapter, "build_orders_for_tge", None)
        if callable(build_orders):
            orders = build_orders(signal, getattr(self._strategy, "config", None))
            open_orders = self._adapter.get_open_orders()
            positions = self._adapter.get_positions()
            filtered = self._risk.filter_orders(orders, open_orders, positions)
            if filtered:
                self._executor.submit_orders(filtered)
            return filtered
        if not orders:
            markets = self._adapter.search_markets(self._config.search_query, self._config.search_limit)
            quotes = [self._adapter.get_quote(m.id) for m in markets]
            orders = self._strategy.generate_orders(signal, markets, quotes)

        open_orders = self._adapter.get_open_orders()
        positions = self._adapter.get_positions()
        filtered = self._risk.filter_orders(orders, open_orders, positions)
        if filtered:
            self._executor.submit_orders(filtered)
        return filtered
