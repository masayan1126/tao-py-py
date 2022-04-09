from typing import Dict
import pandas as pd


class XCsv:

    # csvを読み取り、dfを返します
    def read(self, filepath, encoding, header, sep=","):
        try:
            return pd.read_csv(filepath, encoding=encoding, header=header, sep=sep)
        except FileNotFoundError:
            raise FileNotFoundError

    # dfを読み取り、csvをに出力します
    def output(self, filepath, dict: Dict):
        try:
            df = pd.DataFrame(dict)
            df.to_csv(filepath, encoding="utf_8_sig")
        except FileNotFoundError:
            raise FileNotFoundError
