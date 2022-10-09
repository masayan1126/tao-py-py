from dataclasses import dataclass
import re
from shared.Domain.String.xstr import XStr


@dataclass
class XRegex:
    _target: XStr

    def target(self):
        return self._target

    # 先頭に限らずマッチ部分を返します(部分一致)
    def partial_match(self, pattern: XStr):
        match = re.search(pattern.value(), self.target().value())

        if match is None:
            return match

        return match.group()

    # targetをreplacementで置換した結果を返します
    def replace(self, pattern: XStr, replacement: str):
        return re.sub(pattern.value(), replacement, self.target().value())
