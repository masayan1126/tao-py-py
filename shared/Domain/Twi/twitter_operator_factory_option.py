from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TwitterOperatorFactoryOption:
    _screen_name: str
    _black_list: list[str]

    def __init__(self, screen_name: str, black_list: list[str]):
        self._screen_name = screen_name
        self._black_list = black_list

    def screen_name(self) -> str:
        return self._screen_name

    def black_list(self) -> list[str]:
        return self._black_list
