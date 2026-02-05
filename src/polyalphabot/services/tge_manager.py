from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Set, Tuple

from polyalphabot.models.entities import TgeSignal
from polyalphabot.services.tge_source import TgeSource


@dataclass
class TgeManager:
    sources: List[TgeSource]

    def poll(self) -> List[TgeSignal]:
        signals: List[TgeSignal] = []
        seen: Set[Tuple[str, str]] = set()
        for source in self.sources:
            for signal in source.poll():
                key = (signal.token_symbol.lower(), signal.token_name.lower())
                if key in seen:
                    continue
                seen.add(key)
                signals.append(signal)
        return signals
