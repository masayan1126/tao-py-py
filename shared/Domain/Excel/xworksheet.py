from pandas import DataFrame


class XWorksheet:
    def __init__(self, df: DataFrame):
        self.df = df

    # 特定のセル df.at[row, column]
    def get_cell(self, index_number, column_number):
        return self.df.iat[index_number, column_number]

    # 1レコード df.loc[row]
    def get_record(self, index):
        return self.df.loc[index]

    # 複数レコード範囲指定 df.iloc[start_row, end_row, start_column, end_column]
    def get_records(self, start_row, end_row, start_column, end_column):
        return self.df.iloc[start_row:end_row, start_column:end_column]