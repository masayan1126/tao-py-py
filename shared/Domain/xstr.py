class XStr:
    def __init__(self, string: str):
        self.string = string

    def get_string(self):
        return str.strip(self.string)

    def is_contain(self, other):
        return other in self.get_string()

    def has_begin(self, other: str):
        return self.get_string().startswith(other)

    def has_end(self, other: str):
        return self.get_string().endswith(other)
