from __future__ import annotations

from typing import List, Optional

from polyalphabot.adapters.base import PredictionMarketAdapter
from polyalphabot.models.entities import Market, Order, OrderRequest, Position, Quote, Trade


class OpinionAdapter(PredictionMarketAdapter):
    """Placeholder adapter for Opinion market."""

    def __init__(self, api_key: str | None = None) -> None:
        self._api_key = api_key

    def name(self) -> str:
        return "opinion"

    def search_markets(self, query: str, limit: int = 50) -> List[Market]:
        raise NotImplementedError("Implement search for Opinion.")

    def get_market(self, market_id: str) -> Market:
        raise NotImplementedError("Implement get_market for Opinion.")

    def get_quote(self, market_id: str) -> Quote:
        raise NotImplementedError("Implement quote for Opinion.")

    def place_order(self, request: OrderRequest) -> Order:
        raise NotImplementedError("Implement order for Opinion.")

    def cancel_order(self, order_id: str) -> None:
        raise NotImplementedError("Implement cancel for Opinion.")

    def get_open_orders(self) -> List[Order]:
        raise NotImplementedError("Implement open orders for Opinion.")

    def get_positions(self) -> List[Position]:
        raise NotImplementedError("Implement positions for Opinion.")

    def get_trades(self, market_id: Optional[str] = None) -> List[Trade]:
        raise NotImplementedError("Implement trades for Opinion.")
