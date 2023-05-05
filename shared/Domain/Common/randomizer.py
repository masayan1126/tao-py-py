import random

class Randomizer:
    def gen_random_int(self, start: int, end: int) -> int:
        return random.randint(start, end)