import os
from shared.Domain.FileSystem.x_folder import XFolder


class MakeFolderReciver:
    def __str__(self):
        pass

    def action(self, xfolder: XFolder) -> None:
        os.makedirs(xfolder.get_folder_path(), exist_ok=True)
