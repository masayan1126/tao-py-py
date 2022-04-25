# 読み込み(r または rt)
# 書き込み(w または wt)
# 追記(a または at)

from typing import IO, List
from shared.Domain.Text.x_text import XText


class TextFileOperator:
    def __init__(self, x_text: XText):
        self.x_text = x_text

    def _open(self, mode: str, encoding: str) -> IO:
        try:
            f = open(self.x_text.filepath().of_text(), mode=mode, encoding=encoding)
            return f
        except FileNotFoundError:
            raise FileNotFoundError

    def read(self, encoding: str) -> str:
        try:
            f = self._open(mode="r", encoding=encoding)
            return f.read()
        except FileNotFoundError:
            raise FileNotFoundError
        finally:
            if "f" in locals():
                f.close()

    def readline(self, encoding: str) -> List[str]:
        try:
            f = self._open(mode="r", encoding=encoding)
            return [s.strip() for s in f.readlines()]
        except FileNotFoundError:
            raise FileNotFoundError
        finally:
            if "f" in locals():
                f.close()

    def write(self, content: str, is_overwrite: False, encoding) -> str:
        # 上書き
        if is_overwrite:
            mode = "w"
        # 追記
        else:
            mode = "a"

        try:
            f = self._open(mode=mode, encoding=encoding)
            f.write(content)
            # 書き込み後に最新のテキスト情報を返す
            f = self._open(mode="r", encoding=encoding)
            return f.read()
        except FileNotFoundError:
            raise FileNotFoundError
        finally:
            if "f" in locals():
                f.close()
