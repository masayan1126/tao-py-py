import re
from shared.Domain.Regex.xregex import XRegex
from shared.Domain.String.xstr import XStr

# 正規表現に一致する文字列が含まれていればその文字列のマッチする部分を、含まれていなければ、文字列をそのまま返します
class RegexService:
    def check(self, regex: XRegex, xstr: XStr):
        match = re.findall(regex.pattern(), xstr.value())
        if len(match) > 0:
            return match[0]
        else:
            return xstr.value()

    # 置換
    def substitute(self, regex: XRegex, target: XStr, replacement: str):
        return XRegex(regex.pattern()).substitute(target, replacement)
