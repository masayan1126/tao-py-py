import abc
from shared.Core.reciver import Receiver


class Command:
    @abc.abstractmethod
    def set_reciver(self, receiver: Receiver):
        self.reciver = receiver

    @abc.abstractmethod
    def execute(self) -> None:
        pass
