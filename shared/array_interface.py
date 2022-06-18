from __future__ import annotations
import abc

from shared.Domain.String.xstr import XStr


class ArrayInterface:
    @abc.abstractmethod
    # 元のリストを返します
    def all() -> list:
        pass

    @abc.abstractmethod
    # 元のリストをn個に分割したリストにして返します
    def split(number: int) -> ArrayInterface:
        pass

    @abc.abstractmethod
    # リスト内の文字列を結合した1つの文字列にして返します
    def to_str(number: int) -> XStr:
        pass
