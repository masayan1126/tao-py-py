from pandas import DataFrame

from shared.Domain.xworksheet import XWorksheet


class XWorkbook:
    def __init__(self, df: DataFrame):
        self.df = df

    def get_all_sheet_names(self):
        return list(self.df.keys())

    def get_all_sheet_values(self):
        return list(self.df.values())

    def get_sheet_by_name(self, sheetname) -> XWorksheet:
        return XWorksheet(self.df[sheetname])
