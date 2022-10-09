from dataclasses import dataclass
import os
from shared.Domain.Url.x_url import XUrl


@dataclass
class XFile:
    def __init__(self, x_url: XUrl):
        self._x_url = x_url

    def filepath(self) -> XUrl:
        return self._x_url

    # ファイル名を返します(拡張子あり、クエリストリングは含まない)
    def filename(self) -> str:
        return os.path.basename(self.filepath().href())

    # 拡張子を返します
    def extension(self) -> str:
        return os.path.splitext(self.filename())[1]
