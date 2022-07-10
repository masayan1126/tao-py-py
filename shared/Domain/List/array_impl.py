from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable
from shared.Domain.String.xstr import XStr
from shared.array_interface import ArrayInterface


@dataclass
class ArrayImpl(ArrayInterface):
    array: list

    # 元のリストを返します
    def all(self) -> list:
        return self.array

    def add(self, item: Any) -> ArrayImpl:
        self.array.append(item)
        return self

    def map(self, callable: Callable) -> ArrayImpl:
        return ArrayImpl(list(map(lambda item: callable(item), self.all())))

    def first(self) -> Any:
        try:
            return self.all()[0]
        except IndexError:

            raise IndexError

    def count(self) -> int:
        return len(self.array)

    def is_empty(self) -> bool:
        return self.count() == 0

    # 元のリストをn個に分割したリストにして返します
    def split(self, n: int) -> ArrayInterface:
        return ArrayImpl([self.array[i : i + n] for i in range(0, len(self.array), n)])

    # リスト内の文字列を結合した1つの文字列にして返します
    def to_str(self) -> XStr:
        joined = ""
        for s in self.all():
            if not isinstance(s, str):
                raise TypeError(f"{s} is not str type")
            joined += s
        return XStr(joined)
