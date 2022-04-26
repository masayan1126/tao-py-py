import random
from typing import List
from shared.Domain.i_randomizer import IRamdomizer


class NumberRandomizer(IRamdomizer):
    # def __init__(self, string: str):

    # def __str__(self):
    #     return f"文字列: {self.string}"

    # def __eq__(self, other):
    #     if not isinstance(other, XStr):
    #         return NotImplemented
    #     return self.string == other.string

    # def __lt__(self, other):
    #     if not isinstance(other, XStr):
    #         return NotImplemented
    #     return self.string < other.string

    def generate(self, min: int = 0, max: int = 1, count: int = 1) -> List[int]:
        # minからmaxの範囲でcountの数だけ重複のないランダムな整数のリストを返します
        return random.sample(range(min, max), k=count)
