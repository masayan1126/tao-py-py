import random
from shared.Domain.i_randomizer import IRamdomizer


class NumberRandomizer(IRamdomizer):
    def generate(self, min: int = 0, max: int = 1, count: int = 1) -> list[int]:
        # minからmaxの範囲でcountの数だけ重複のないランダムな整数のリストを返します
        return random.sample(range(min, max), k=count)
