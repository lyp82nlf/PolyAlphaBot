from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional


class OrderSide(str, Enum):
    BUY = "buy"
    SELL = "sell"


class OrderType(str, Enum):
    LIMIT = "limit"
    MARKET = "market"


@dataclass(frozen=True)
class Market:
    id: str
    name: str
    description: str
    tags: List[str] = field(default_factory=list)
    base_token: Optional[str] = None
    quote_token: Optional[str] = None
    is_active: bool = True
    event_datetime: Optional[datetime] = None
    metadata: Dict[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class Quote:
    market_id: str
    best_bid: Optional[float]
    best_ask: Optional[float]
    midpoint: Optional[float]
    timestamp: datetime


@dataclass(frozen=True)
class OrderRequest:
    market_id: str
    side: OrderSide
    quantity: float
    price: Optional[float] = None
    order_type: OrderType = OrderType.LIMIT
    client_order_id: Optional[str] = None


@dataclass(frozen=True)
class Order:
    id: str
    market_id: str
    side: OrderSide
    quantity: float
    price: Optional[float]
    order_type: OrderType
    status: str
    created_at: datetime


@dataclass(frozen=True)
class Position:
    market_id: str
    quantity: float
    average_price: float
    unrealized_pnl: Optional[float] = None


@dataclass(frozen=True)
class Trade:
    id: str
    market_id: str
    side: OrderSide
    quantity: float
    price: float
    timestamp: datetime


@dataclass(frozen=True)
class TgeSignal:
    token_symbol: str
    token_name: str
    chain: Optional[str]
    launch_time: Optional[datetime]
    confidence: float
    raw: Dict[str, object] = field(default_factory=dict)
