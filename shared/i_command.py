import abc

from shared.i_reciver import IReceiver


class ICommand:
    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def setReciver(self, receiver: IReceiver):
        self.reciver = receiver

    @abc.abstractmethod
    def execute(self) -> None:
        pass
