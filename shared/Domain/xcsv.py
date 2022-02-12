import pandas as pd


class XCsv:

    # csvを読み取り、dfを返します
    def read(self, filepath, encoding, header, sep):
        try:
            return pd.read_csv(filepath, encoding=encoding, header=header, sep=sep)
        except FileNotFoundError:
            print("対象のファイルが存在しないか、破損しています")

    # dfを読み取り、csvをに出力します
    def output(filepath, df: pd.DataFrame):
        try:
            df.to_csv(filepath)
        except FileNotFoundError:
            print("対象のファイルが存在しないか、破損しています")
