import io, sys
from shared.Application.make_folder_service import MakeFolderService
from shared.Domain.xfolder import XFolder
from shared.Domain.xcsv import XCsv

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

# フォルダ作成
list(
    map(
        lambda folder_name: MakeFolderService().execute(
            XFolder(base_path, folder_name)
        ),
        folder_name_list,
    )
)
