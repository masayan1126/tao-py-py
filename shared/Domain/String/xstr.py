from __future__ import annotations
from dataclasses import dataclass
from shared.Exception.empty_string_error import EmptyStringError


@dataclass
class XStr:
    _value: str

    def __init__(self, value: str):
        # 空文字の場合
        if len(value) == 0:
            raise EmptyStringError("Empty string cannot be specified")

        self._value = value

    def value(self) -> str:
        return str.strip(self._value)

    def is_contain(self, other: str) -> bool:
        return other in self.value()

    def has_begin(self, other: str) -> bool:
        return self.value().startswith(other)

    def has_end(self, other: str) -> bool:
        return self.value().endswith(other)

    def count(self) -> int:
        return len(self.value())

    def to_list(self, sep: str = None) -> list[str]:
        # セパレータが指定なしなら、単に文字列を1文字ずつ区切った配列にして返す
        if sep is None:
            return list(self.value())
        else:
            # セパレータあり("," など)
            return self.value().split(sep)

    def join(self, other: str = "\n") -> XStr:
        self._value = self._value + other
        return self

    def to_upper(self) -> XStr:
        return XStr(self.value().upper())

    def to_lower(self) -> XStr:
        return XStr(self.value().lower())

    # 文字も位置も一致している文字の数を返します
    def compare(self, other: str) -> int:
        if self.count() != len(other):
            raise ValueError

        result = 0

        for char in self.value():
            if char in self.value() and self.value().find(char) == other.find(char):
                result += 1

        return result
