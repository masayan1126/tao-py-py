from typing import Dict, Tuple
import pandas as pd

from shared.Domain.Excel.xworkbook import XWorkbook
from shared.Domain.x_file_system_path import XFileSystemPath


# 使用するエクセルのフォーマットルール
# - 各シートにヘッダーがある
# - 各シートに一番左の列に1から始まる連番ないしID列がある
# - 各シートにシート名がある
# - indexはもともと用意されている0始まりの連番を使用する(エクセルの実際のカラムをindexとして使用しない)
class XExcel:
    # エクセルを読み取ります
    def read(
        self,
        filepath: XFileSystemPath,
        # 基本はすべてのシートが読み込むためNoneで指定
        sheet_name: str = None,
        # デフォルトはヘッダ行は0行目とする
        header_row_number: int = 0,
        # index行はデフォルトのまま、0始まりの連番とする
        index_col: int = None,
    ) -> XWorkbook:
        try:
            return XWorkbook(
                pd.read_excel(
                    filepath.of_text(),
                    sheet_name=sheet_name,
                    header=header_row_number,
                    index_col=index_col,
                )
            )
        except FileNotFoundError:
            raise FileNotFoundError

        except PermissionError:
            raise PermissionError

    # dfをエクセルに出力します
    def output(self, filepath: XFileSystemPath, data: Dict) -> None:

        # {"id": [1, 2, 3,4], "name": ["PHP", "Java", "Python", "Ruby"], "type": ["動的型付け", "静的型付け","動的型付け","動的型付け"]}
        # 辞書のキーをdataframeのカラムにしたいので、orientにindexを指定
        df = pd.DataFrame.from_dict(data, orient="index").T

        try:
            return df.to_excel(
                filepath.of_text(),
                # インデックスは出力しなくてよいので、Falseで指定
                index=False,
            )
        except FileNotFoundError:
            raise FileNotFoundError
