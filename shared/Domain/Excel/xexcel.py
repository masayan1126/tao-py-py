import pandas as pd

from shared.Domain.Excel.xworkbook import XWorkbook


class XExcel:

    # csvを読み取り、dfを返します
    def read(self, filepath, sheet_name) -> XWorkbook:
        try:
            return XWorkbook(pd.read_excel(filepath, sheet_name=sheet_name))
        except FileNotFoundError:
            raise FileNotFoundError

    # dfを読み取り、csvをに出力します
    def output(filepath, df: pd.DataFrame):
        try:
            df.to_csv(filepath)
        except FileNotFoundError:
            raise FileNotFoundError
