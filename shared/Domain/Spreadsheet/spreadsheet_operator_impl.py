from __future__ import annotations
from dataclasses import dataclass


@dataclass
class SpreadsheetOperatorImpl:
    def sample(self, x: int, y: int, duration: int, wait_time: float = None) -> None:
        pass
