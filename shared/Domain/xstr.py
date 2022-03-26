from shared.base_class import BaseClass
from shared.Exception.empty_string_error import EmptyStringError


class XStr(BaseClass):
    def __init__(self, string: str):
        if not isinstance(string, str):
            raise TypeError
        # 空文字の場合
        if len(string) == 0:
            raise EmptyStringError("空文字は指定できません")

        self.string = string

    def __str__(self):
        return f"文字列: {self.string}"

    def __eq__(self, other):
        if not isinstance(other, XStr):
            return NotImplemented
        return self.string == other.string

    def __lt__(self, other):
        if not isinstance(other, XStr):
            return NotImplemented
        return self.string < other.string

    def get_string(self):
        return str.strip(self.string)

    def is_contain(self, other):
        return other in self.get_string()

    def has_begin(self, other: str):
        return self.get_string().startswith(other)

    def has_end(self, other: str):
        return self.get_string().endswith(other)

    def count(self):
        return len(self.get_string())

    def to_list(self, sep=","):
        return self.get_string().split(sep)
