import re
from shared.Domain.xregex import XRegex
from shared.Domain.xstr import XStr

# 正規表現に一致する文字列が含まれていればその文字列のマッチする部分を、含まれていなければ、文字列をそのまま返します
class CheckRegexService:
    def execute(self, regex: XRegex, xstr: XStr):
        match = re.findall(regex.pattern(), xstr.get_string())
        if len(match) > 0:
            return match[0]
        else:
            return xstr.get_string()
