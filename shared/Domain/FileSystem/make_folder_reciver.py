import os
from shared.Domain.FileSystem.x_folder import XFolder
from shared.i_command import ICommand


class MakeFolderReciver(ICommand):
    def __str__(self):
        pass

    def action(self, xfolder: XFolder) -> None:
        os.makedirs(xfolder.get_folder_path(), exist_ok=True)
