import os

from shared.Domain.Url.x_url import XUrl
from shared.Domain.xregex import XRegex
from shared.Application.check_regex_service import CheckRegexService
from shared.Domain.xstr import XStr


class XFile:
    def __init__(self, x_url: XUrl):
        self._x_url = x_url

    def x_url(self) -> XUrl:
        return self._x_url

    # ファイル名を返します(拡張子あり、クエリストリングは含まない)
    def filename(self) -> str:

        file_name = CheckRegexService().execute(
            XRegex(".+?(?=\?)"), xstr=XStr(self.x_url().href())
        )

        return os.path.basename(file_name)

    # 拡張子を返します
    def extension(self) -> str:
        return os.path.splitext(self.filename())[1]
