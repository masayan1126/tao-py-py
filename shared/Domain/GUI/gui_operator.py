from __future__ import annotations
from abc import ABCMeta, abstractmethod


class GUIOperator(metaclass=ABCMeta):
    @abstractmethod
    def click(
        self, x: int, y: int, duration: int, wait_time: float, loop_count: int = 1
    ) -> GUIOperator:
        pass

    @abstractmethod
    def pressKey(self, key_name: str) -> None:
        pass

    @abstractmethod
    def scroll(self, amount: int) -> None:
        pass

    @abstractmethod
    def shortcut(
        self,
        key1: str,
        key2: str = None,
        key3: str = None,
        wait_time: float = None,
        loop_count: int = 1,
    ) -> None:
        pass

    @abstractmethod
    def copy(
        self,
        string: str,
        wait_time: float = None,
    ) -> None:
        pass

    @abstractmethod
    def get_position(
        self,
    ) -> tuple[int]:
        pass
