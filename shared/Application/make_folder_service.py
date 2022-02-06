import os
from shared.Domain.xfolder import XFolder


class MakeFolderService:
    def execute(self, xfolder: XFolder):
        os.makedirs(xfolder.get_folder_path(), exist_ok=True)
