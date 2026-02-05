from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from polyalphabot.models.entities import TgeSignal


class TgeSource(ABC):
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def poll(self) -> Iterable[TgeSignal]:
        raise NotImplementedError
