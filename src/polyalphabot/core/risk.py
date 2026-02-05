from __future__ import annotations

from dataclasses import dataclass
from typing import List

from polyalphabot.models.entities import Order, OrderRequest, Position


@dataclass(frozen=True)
class RiskConfig:
    max_open_orders: int = 20
    max_positions: int = 20
    max_position_size: float = 1000.0
    max_total_exposure: float = 5000.0


class RiskManager:
    def __init__(self, config: RiskConfig) -> None:
        self._config = config

    def filter_orders(
        self,
        orders: List[OrderRequest],
        open_orders: List[Order],
        positions: List[Position],
    ) -> List[OrderRequest]:
        if not orders:
            return []

        exposure = sum(p.quantity * p.average_price for p in positions)
        filtered: List[OrderRequest] = []
        for order in orders:
            if len(open_orders) + len(filtered) >= self._config.max_open_orders:
                break
            if len(positions) >= self._config.max_positions:
                break
            if order.quantity * (order.price or 0) > self._config.max_position_size:
                continue
            if exposure + order.quantity * (order.price or 0) > self._config.max_total_exposure:
                continue
            filtered.append(order)
            exposure += order.quantity * (order.price or 0)
        return filtered
