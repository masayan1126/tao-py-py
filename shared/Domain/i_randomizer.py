from abc import *


class IRamdomizer(metaclass=ABCMeta):
    @abstractmethod
    def generate(self) -> None:
        pass
