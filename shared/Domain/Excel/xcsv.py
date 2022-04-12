from typing import Dict
import pandas as pd

from shared.Domain.x_file_system_path import XFileSystemPath


class XCsv:

    # csvを読み取り、dfを返します
    def read(self, filepath: XFileSystemPath, encoding, header, sep=","):
        try:
            return pd.read_csv(
                filepath.of_text(), encoding=encoding, header=header, sep=sep
            )
        except FileNotFoundError:
            raise FileNotFoundError

    # dfを読み取り、csvをに出力します
    def output(self, filepath: XFileSystemPath, dict: Dict):
        try:
            df = pd.DataFrame(dict)
            df.to_csv(filepath.of_text(), encoding="utf_8_sig")
        except FileNotFoundError:
            raise FileNotFoundError
