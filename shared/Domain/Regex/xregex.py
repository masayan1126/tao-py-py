import re
from shared.Domain.String.xstr import XStr


class XRegex:
    def __init__(self, pattern: str):
        self._pattern = pattern

    def pattern(self):
        return self._pattern

    # 先頭に限らずマッチ部分を返す(部分一致)
    def partial_match(self, target: XStr):
        match = re.search(self.pattern(), target.value())
        return match.group()

    # targetをreplacementで置換した結果を返します
    def substitute(self, target: XStr, replacement: str):
        return re.sub(self.pattern(), replacement, target.value())
