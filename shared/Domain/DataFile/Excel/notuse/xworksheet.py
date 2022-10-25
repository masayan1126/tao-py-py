from pandas import DataFrame


# 使用するエクセルは
# - 行番号は実際のエクセルの行番号を指定する
class XWorksheet:
    def __init__(self, df: DataFrame):
        self.df = df

    # 特定のセルを行番号・列番号を指定して取得
    # 行・列が0始まりなので、行はヘッダ行分と合わせて2マイナスする。列はiatが0始まりなのでマイナス1すると実際のエクセルの行・列番号を指定する形でよくなる
    def get_cell(self, index_number, column_number):
        return self.df.iat[index_number - 2, column_number - 1]

    # 1レコード df.iloc[row]
    def get_record(self, index):
        # ilocが0始まりなのと、ヘッダ行分の1行の合わせて2行分をマイナスすると実際のエクセルの行番号を指定する形でよくなる
        # 1行のレコードは、辞書型で取得する
        try:
            return self.df.iloc[index - 2].to_dict()
        except IndexError as e:
            raise e

    # 複数レコード範囲指定 df.iloc[start_row, end_row, start_column, end_column]
    # 行番号・列番号は0はじまり
    # actual = setuped_worksheet.get_records(3, 4, 1, 3)
    def get_records_with_filter(
        self, start_row, end_row, start_column, end_column, expression
    ):
        df = self.df.query(expression)
        return df.iloc[
            start_row - 2 : end_row - 1, start_column - 1 : end_column
        ].to_dict("records")

    def get_records(self, start_row, end_row, start_column, end_column):
        return self.df.iloc[
            start_row - 2 : end_row - 1, start_column - 1 : end_column
        ].to_dict("records")

    def all_records(self):
        return self.df.iloc[:, :].to_dict("records")
