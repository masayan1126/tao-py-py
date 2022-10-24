from shared.Domain.DataFile.Csv.csv_file_operator_impl import CsvFileOperatorImpl
from shared.Domain.FileSystem.make_folder_command import MakeFolderCommand
from shared.Domain.FileSystem.make_folder_reciver import MakeFolderReciver
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.FileSystem.x_folder import XFolder
from shared.Domain.FileSystem.x_folder_aggregate import XFolderAggregate
from shared.Domain.String.xstr import XStr
from shared.Core.aggregate import Aggregate
from shared.Core.command import Command
from shared.Core.iterator import Iterator


class FolderMakeUsecase:
    def __init__(self, folder_list_path: XFileSystemPath):
        self.folder_list_path = folder_list_path

    def make(self):
        command: Command = MakeFolderCommand()
        command.set_reciver(MakeFolderReciver())
        aggregate: Aggregate = XFolderAggregate()

        for folder_name in self.folder_name_list():
            aggregate.add_item(XFolder(XFileSystemPath(XStr(folder_name))))

        iterator: Iterator = aggregate.iterator()

        while iterator.has_next():
            item = iterator.next()
            command.execute(item)

    def folder_name_list(self) -> list[str]:
        # csv読み込み(# TODO:取り込むcsvのフォーマットのルールを設ける必要がある)
        dirs_df = CsvFileOperatorImpl().read(
            filepath=self.folder_list_path,
            encoding="shift-jis",
            header=0,
        )
        column = "name"
        return dirs_df[column].to_list()
