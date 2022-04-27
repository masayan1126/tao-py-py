from shared.Domain.File.x_file import XFile


class XImage:
    def __init__(self, x_file: XFile):
        self._x_file = x_file

    def x_file(self) -> XFile:
        return self._x_file
