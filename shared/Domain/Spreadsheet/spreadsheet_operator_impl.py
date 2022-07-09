from __future__ import annotations
from dataclasses import dataclass
from time import sleep
import pyautogui as pgui


@dataclass
class SpreadsheetOperatorImpl:
    def sample(self, x: int, y: int, duration: int, wait_time: float = None) -> None:
        pass
