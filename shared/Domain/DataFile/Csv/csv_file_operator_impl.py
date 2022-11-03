from dataclasses import dataclass
import pandas as pd

# memo: テストでこのimport文を使用しているので注意
from pandas import DataFrame

from pandas import read_table
from codecs import open
from shared.Domain.DataFile.data_file_operator import DataFileOperator
from shared.Domain.DataFile.data_frame_converter import DataFrameConverter
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath


@dataclass
class CsvFileOperatorImpl(DataFileOperator):
    """使用するCSVのフォーマットルール
    - ヘッダー行が先頭にあり
    - インデックス列なし(最左列)
    """

    def _open(
        self,
        filepath: XFileSystemPath,
        encoding: str = "UTF-8",  # shift-jis
    ):

        return open(
            # ignoreは、文字コードエラーで読めなかった文字だけスキップする
            filepath.to_text(),
            mode="r",
            encoding=encoding,
            errors="ignore",
        )

    def read(
        self,
        filepath: XFileSystemPath,
        encoding: str = "UTF-8",  # shift-jis
        sep=",",
    ) -> list:

        try:
            file = self._open(filepath)

            return DataFrameConverter.to_list(
                # headerは0始まりでデフォルト0(0だと、最初の行がヘッダーになる)
                # index_colは0始まりでindexとして使いたい列の列番号を指定する(indexに指定した列のデータは、取得するDataFrameのデータに含まれない)
                read_table(file, sep=sep, header=0, index_col=None)
            )

        finally:
            file.close()

    # 辞書オブジェクトのリストをcsvに出力します
    def output(
        self,
        filepath: XFileSystemPath,
        data_list: list,
        index=False,
        encoding: str = "utf-8-sig",
        mode: str = "w",
    ):

        pd.DataFrame(data_list).to_csv(
            filepath.to_text(),
            encoding=encoding,
            index=index,
            errors="ignore",
            mode=mode,  # 追記
        )
