import os

from shared.Domain.Url.x_url import XUrl
from shared.Domain.Regex.xregex import XRegex
from shared.Domain.Regex.check_regex_service import CheckRegexService
from shared.Domain.String.xstr import XStr


class XFile:
    def __init__(self, x_url: XUrl):
        self._x_url = x_url

    def x_url(self) -> XUrl:
        return self._x_url

    # ファイル名を返します(拡張子あり、クエリストリングは含まない)
    def filename(self) -> str:

        file_name = CheckRegexService().check(
            XRegex(".+?(?=\?)"), xstr=XStr(self.x_url().href())
        )

        return os.path.basename(file_name)

    def filename_with_queryst(self) -> str:
        return os.path.basename(self.x_url().href())

    # 拡張子を返します
    def extension(self) -> str:
        return os.path.splitext(self.filename())[1]
