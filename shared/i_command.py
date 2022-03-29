import abc
from shared.i_reciver import IReceiver


class ICommand:
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def set_reciver(self, receiver: IReceiver):
        self.reciver = receiver

    @abc.abstractmethod
    def execute(self) -> None:
        pass
