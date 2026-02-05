from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable, List, Optional

from polyalphabot.models.entities import Market, Order, OrderRequest, Position, Quote, Trade


class PredictionMarketAdapter(ABC):
    """Abstract interface for any prediction market."""

    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def search_markets(self, query: str, limit: int = 50) -> List[Market]:
        raise NotImplementedError

    @abstractmethod
    def get_market(self, market_id: str) -> Market:
        raise NotImplementedError

    @abstractmethod
    def get_quote(self, market_id: str) -> Quote:
        raise NotImplementedError

    @abstractmethod
    def place_order(self, request: OrderRequest) -> Order:
        raise NotImplementedError

    @abstractmethod
    def cancel_order(self, order_id: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_open_orders(self) -> List[Order]:
        raise NotImplementedError

    @abstractmethod
    def get_positions(self) -> List[Position]:
        raise NotImplementedError

    @abstractmethod
    def get_trades(self, market_id: Optional[str] = None) -> List[Trade]:
        raise NotImplementedError

    def close(self) -> None:
        pass
