from abc import ABCMeta, abstractmethod


class IRamdomizer(metaclass=ABCMeta):
    @abstractmethod
    def generate(self) -> None:
        pass
