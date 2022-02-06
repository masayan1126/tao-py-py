import os

from shared.Domain.xurl import XUrl
from shared.Domain.xregex import XRegex
from shared.Application.check_regex_service import CheckRegexService
from shared.Domain.xstr import XStr


class XFile:
    def __init__(self, x_url: XUrl):
        self.x_url = x_url

    def get_url(self):
        return self.x_url

    # ファイル名を返します(クエリストリングは含まない)
    def get_file_name(self):

        file_name = CheckRegexService().execute(
            XRegex(".+?(?=\?)"), xstr=XStr(self.x_url.get_href())
        )

        return os.path.basename(file_name)

    def get_alt(self):
        return self.alt

    # 拡張子を返します
    def get_extension(self):
        return os.path.splitext(self.get_file_name())[1]
