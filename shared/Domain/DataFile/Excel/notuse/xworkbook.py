from dataclasses import dataclass
from pandas import DataFrame
from shared.Domain.DataFile.Excel.notuse.xworkbook import XWorksheet


@dataclass
class XWorkbook:

    # シート名がキーkey、そのシートのデータpandas.DataFrameが値valueとなる辞書dict
    def __init__(self, df: DataFrame):
        self.df = df

    def get_all_sheet_names(self) -> list:
        return list(self.df.keys())

    def get_all_sheet_values(self) -> list:
        return list(self.df.values())

    def get_sheet_by_name(self, sheetname: str) -> XWorksheet:
        return XWorksheet(self.df[sheetname])
