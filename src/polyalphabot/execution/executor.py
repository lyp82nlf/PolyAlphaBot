from __future__ import annotations

from typing import List

from polyalphabot.adapters.base import PredictionMarketAdapter
from polyalphabot.models.entities import Order, OrderRequest


class Executor:
    def __init__(self, adapter: PredictionMarketAdapter) -> None:
        self._adapter = adapter

    def submit_orders(self, orders: List[OrderRequest]) -> List[Order]:
        results: List[Order] = []
        if not orders:
            return results
        # Using adapter logging for per-order details.
        for order in orders:
            results.append(self._adapter.place_order(order))
        return results
