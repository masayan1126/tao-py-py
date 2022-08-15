import pandas as pd
import codecs
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath


class XCsv:

    # csvを読み取り、dfを返します
    def read(
        self,
        filepath: XFileSystemPath,
        encoding: str = "shift-jis",
        header: int = 0,
        sep=",",
        index_col=None,
    ):

        try:
            with codecs.open(
                filepath.of_text(), mode="r", encoding=encoding, errors="ignore"
            ) as file:
                return pd.read_table(file, sep=sep, header=header, index_col=index_col)
            # return pd.read_csv(
            #     filepath.of_text(),
            #     encoding=encoding,
            #     header=header,
            #     sep=sep,
            #     index_col=index_col,
            # )
        except FileNotFoundError:
            raise FileNotFoundError

    # dfを読み取り、csvをに出力します
    def output(
        self,
        filepath: XFileSystemPath,
        dict: dict,
        index=False,
        encoding: str = "utf-8-sig",
    ):
        try:
            df = pd.DataFrame(dict)
            df.to_csv(
                filepath.of_text(), encoding=encoding, index=index, errors="ignore"
            )
        except FileNotFoundError:
            raise FileNotFoundError
