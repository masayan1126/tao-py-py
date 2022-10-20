from shared.Domain.FileSystem.x_folder import XFolder
from shared.Core.command import Command
from shared.Core.i_reciver import IReceiver


class MakeFolderCommand(Command):
    def __init__(self):
        pass

    def set_reciver(self, receiver: IReceiver):
        self.reciver = receiver

    def execute(self, xfolder: XFolder) -> None:
        self.reciver.action(xfolder)
