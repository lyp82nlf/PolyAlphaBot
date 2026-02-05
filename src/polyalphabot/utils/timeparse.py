from __future__ import annotations

from datetime import datetime
from typing import Optional


def parse_datetime(value: object) -> Optional[datetime]:
    if not value:
        return None
    text = str(value)
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
