import os
from shared.Domain.xfolder import XFolder
from shared.i_command import ICommand
from shared.i_reciver import IReceiver


class MakeFolderCommand(ICommand):
    def __init__(self):
        pass

    def setReciver(self, receiver: IReceiver):
        self.reciver = receiver

    def execute(self, xfolder: XFolder) -> None:
        self.reciver.action(xfolder)
