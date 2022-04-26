import os
import urllib
from shared.Domain.xregex import XRegex
from shared.Application.check_regex_service import CheckRegexService
from shared.Domain.xstr import XStr
from shared.Domain.Url.x_url import XUrl


class XImage:
    def __init__(self, x_url: XUrl, alt):
        self.x_url = x_url
        self.alt = alt

    def get_url(self):
        return self.x_url

    def get_src(self):
        return self.x_url.href()

    # ファイル名を返します(フォルダ、クエリストリング除く純粋なファイル名をurlデコードしたもの)
    def get_file_name(self):
        file_name = CheckRegexService().execute(
            XRegex(".+?(?=\?)"), xstr=XStr(self.x_url.href())
        )
        return urllib.parse.unquote(os.path.basename(file_name))

    def get_file_name_with_queryst(self):
        return os.path.basename(self.x_url.href())

    def get_alt(self):
        return self.alt
