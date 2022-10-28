from shared.Core.command import Command
from shared.Core.reciver import Receiver


class LoginXserverCommand(Command):
    def set_reciver(self, receiver: Receiver):
        self.reciver = receiver

    def execute(self) -> None:
        self.reciver.action()
