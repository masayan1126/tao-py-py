from abc import *


class SpreadsheetOperator(metaclass=ABCMeta):
    @abstractmethod
    def sample(self, x: int, y: int, duration: int, wait_time: float) -> None:
        pass
