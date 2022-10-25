import pandas as pd
from pandas import read_excel

# memo: テストでこのimport文を使用
import pandas as DataFrame
from shared.Domain.DataFile.data_file_operator import DataFileOperator
from shared.Domain.DataFile.data_frame_converter import DataFrameConverter
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath


class ExcelFileOperatorImpl(DataFileOperator):
    """使用するエクセルのフォーマットルール
    - 各シートにヘッダー行が先頭にあり
    - インデックス列なし(最左列)
    - 各シートにシート名がある
    """

    def read(
        self,
        filepath: XFileSystemPath,
    ) -> list:

        dictionary = read_excel(
            filepath.to_text(),
            # 基本はすべてのシートを読み込むためデフォルトNone
            sheet_name=None,
            # デフォルトはヘッダ行は0行目とする
            header=0,
            # index行はデフォルトのまま、0始まりの連番とする
            index_col=None,
        )

        return [
            {sheetname: DataFrameConverter.to_list(dataframe)}
            for sheetname, dataframe in dictionary.items()
        ]

    def output(
        self,
        filepath: XFileSystemPath,
        sheet_name: str,
        data_list: list,
    ) -> None:

        with pd.ExcelWriter(
            filepath.to_text(),
            mode="a",
            if_sheet_exists="replace",  # すでに存在するシートを指定した場合は置き換え
        ) as writer:
            df = pd.DataFrame(data_list)

            df.to_excel(
                writer,
                sheet_name=sheet_name,
                # インデックスは出力しなくてよいので、Falseで指定
                index=False,
            )
