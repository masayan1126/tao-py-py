from abc import abstractmethod, ABCMeta


class SpreadsheetOperator(metaclass=ABCMeta):
    @abstractmethod
    def sample(self, x: int, y: int, duration: int, wait_time: float) -> None:
        pass
