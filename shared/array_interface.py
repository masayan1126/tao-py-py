from __future__ import annotations
import abc
from typing import Any, Callable

from shared.Domain.String.xstr import XStr


class ArrayInterface:
    @abc.abstractmethod
    # 元のリストを返します
    def all(self) -> list:
        pass

    @abc.abstractmethod
    def add(self, item: Any) -> ArrayInterface:
        pass

    @abc.abstractmethod
    def map(self, callable: Callable) -> ArrayInterface:
        pass

    @abc.abstractmethod
    def first(self) -> Any:
        pass

    @abc.abstractmethod
    def count(self, callback: Callable = None) -> int:
        pass

    @abc.abstractmethod
    def is_empty(self) -> bool:
        pass

    @abc.abstractmethod
    # 元のリストをn個に分割したリストにして返します
    def split(self, n: int) -> ArrayInterface:
        pass

    @abc.abstractmethod
    # リスト内の文字列を結合した1つの文字列にして返します
    def to_str(self) -> XStr:
        pass
