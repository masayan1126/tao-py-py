import io, sys
from packages.make_folder.Domain.make_folder_command import MakeFolderCommand
from packages.make_folder.Domain.make_folder_reciver import MakeFolderReciver
from shared.Domain.xfolder import XFolder
from shared.Domain.Excel.xcsv import XCsv
from shared.i_aggregate import IAggregate
from shared.i_command import ICommand
from shared.i_iterator import IIterator
from shared.x_folder_aggregate import XFolderAggregate

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")


# csv読み込み(# TODO:取り込むcsvのフォーマットのルールを設ける必要がある)
dirs_df = XCsv().read(
    filepath="C:\\Users\\nishigaki\\jupyter-lab\\packages\\make_folder\\list.csv",
    encoding="shift-jis",
    header=0,
)
column = "name"
folder_name_list = dirs_df[column].to_list()
base_path = "C:\\Users\\nishigaki\\Desktop\\test\\"


make_folder_command: ICommand = MakeFolderCommand()
make_folder_command.setReciver(MakeFolderReciver())

x_folder_aggregate: IAggregate = XFolderAggregate()


list(
    map(
        lambda folder_name: x_folder_aggregate.addItem(XFolder(base_path, folder_name)),
        folder_name_list,
    )
)

x_folder_iterator: IIterator = x_folder_aggregate.iterator()

while x_folder_iterator.hasNext():
    item = x_folder_iterator.next()
    make_folder_command.execute(item)
