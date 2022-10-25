from __future__ import annotations
from abc import abstractmethod
from abc import ABCMeta
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class AbstractArray(metaclass=ABCMeta):
    def __init__(self, array: list[Any] = []):
        self.array = array

    # 元のリストを返します
    def all(self) -> list:
        return self.array

    def add(self, item: Any) -> None:
        self.array.append(item)

    @abstractmethod
    def map(self, callable: Callable) -> AbstractArray:
        pass

    def first(self) -> Any:
        try:
            return self.all()[0]
        except IndexError:

            raise IndexError

    def count(self, callback: Callable = None) -> int:
        # コールバックがある場合はその検査に一致する要素の数
        if callback:
            return sum(map(callback, self.array))

        return len(self.array)

    def is_empty(self) -> bool:
        return self.count() == 0
