import abc
from shared.i_reciver import IReceiver


class Command:
    @abc.abstractmethod
    def set_reciver(self, receiver: IReceiver):
        self.reciver = receiver

    @abc.abstractmethod
    def execute(self) -> None:
        pass
