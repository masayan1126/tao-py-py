from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Union
from tqdm import tqdm
from time import sleep


@dataclass
class ProgressBar:
    def __init__(self, completion_criteria: Union[int, list], description: str):

        self.completion_criteria = completion_criteria
        self.description = description

    def run(self, closure: Callable) -> None:

        # リスト
        if isinstance(self.completion_criteria, list):
            self.completion_criteria = len(self.completion_criteria)
            bar = tqdm(total=self.completion_criteria)

        # # 数値
        elif isinstance(self.completion_criteria, int):
            bar = tqdm(total=self.completion_criteria)
            bar.set_description(self.description)

        for i in range(self.completion_criteria):
            sleep(1)
            bar.update(1)
            return closure()
