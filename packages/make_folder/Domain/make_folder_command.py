from shared.Domain.FileSystem.xfolder import XFolder
from shared.i_command import ICommand
from shared.i_reciver import IReceiver


class MakeFolderCommand(ICommand):
    def __init__(self):
        pass

    def set_reciver(self, receiver: IReceiver):
        self.reciver = receiver

    def execute(self, xfolder: XFolder) -> None:
        self.reciver.action(xfolder)
