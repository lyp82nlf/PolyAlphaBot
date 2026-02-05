from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable, List

from polyalphabot.models.entities import Market, OrderRequest, Quote, TgeSignal


class Strategy(ABC):
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def generate_orders(
        self,
        signal: TgeSignal,
        markets: List[Market],
        quotes: List[Quote],
    ) -> List[OrderRequest]:
        raise NotImplementedError
