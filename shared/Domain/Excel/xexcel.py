import pandas as pd

from shared.Domain.Excel.xworkbook import XWorkbook
from shared.Domain.x_file_system_path import XFileSystemPath


class XExcel:

    # csvを読み取り、dfを返します
    def read(
        # デフォルトはヘッダ行は0行目
        self,
        filepath: XFileSystemPath,
        sheet_name,
        header_row_number: int = 0,
    ) -> XWorkbook:
        try:
            return XWorkbook(
                pd.read_excel(
                    filepath.of_text(), sheet_name=sheet_name, header=header_row_number
                )
            )
        except FileNotFoundError:
            raise FileNotFoundError

        except PermissionError:
            raise PermissionError

    # dfを読み取り、csvをに出力します
    def output(filepath, df: pd.DataFrame):
        try:
            df.to_csv(filepath)
        except FileNotFoundError:
            raise FileNotFoundError
