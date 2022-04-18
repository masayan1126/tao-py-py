import io, sys
from packages.make_folder.Domain.make_folder_command import MakeFolderCommand
from packages.make_folder.Domain.make_folder_reciver import MakeFolderReciver
from shared.Domain.x_file_system_path import XFileSystemPath
from shared.Domain.xfolder import XFolder
from shared.Domain.Excel.xcsv import XCsv
from shared.Domain.xstr import XStr
from shared.i_aggregate import IAggregate
from shared.i_command import ICommand
from shared.i_iterator import IIterator
from shared.x_folder_aggregate import XFolderAggregate

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")


# csv読み込み(# TODO:取り込むcsvのフォーマットのルールを設ける必要がある)
dirs_df = XCsv().read(
    filepath=XFileSystemPath(XStr("packages/make_folder/list.csv")).to_absolute(),
    encoding="shift-jis",
    header=0,
)
column = "name"
folder_name_list = dirs_df[column].to_list()
base_path = XFileSystemPath.home_dir().join("Desktop/test")


command: ICommand = MakeFolderCommand()
command.set_reciver(MakeFolderReciver())

aggregate: IAggregate = XFolderAggregate()

xfolder_list = [
    aggregate.add_item(XFolder(base_path.join(folder_name)))
    for folder_name in folder_name_list
]

iterator: IIterator = aggregate.iterator()

while iterator.has_next():
    item = iterator.next()
    command.execute(item)

print("debug")
