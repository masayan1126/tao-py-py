from shared.Domain.Excel.xcsv import XCsv
from shared.Domain.FileSystem.Command.make_folder_command import MakeFolderCommand
from shared.Domain.FileSystem.make_folder_reciver import MakeFolderReciver
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.FileSystem.x_folder import XFolder
from shared.Domain.FileSystem.x_folder_aggregate import XFolderAggregate
from shared.Domain.String.xstr import XStr
from shared.i_aggregate import IAggregate
from shared.Core.command import Command
from shared.i_iterator import IIterator


class FolderMakeUsecase:
    def __init__(self, folder_list_path: XFileSystemPath):
        self.folder_list_path = folder_list_path

    def make(self):
        command: Command = MakeFolderCommand()
        command.set_reciver(MakeFolderReciver())
        aggregate: IAggregate = XFolderAggregate()

        for folder_name in self.folder_name_list():
            aggregate.add_item(XFolder(XFileSystemPath(XStr(folder_name))))

        iterator: IIterator = aggregate.iterator()

        while iterator.has_next():
            item = iterator.next()
            command.execute(item)

    def folder_name_list(self) -> list[str]:
        # csv読み込み(# TODO:取り込むcsvのフォーマットのルールを設ける必要がある)
        dirs_df = XCsv().read(
            filepath=self.folder_list_path,
            encoding="shift-jis",
            header=0,
        )
        column = "name"
        return dirs_df[column].to_list()
