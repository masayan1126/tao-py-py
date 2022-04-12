from shared.Domain.x_file_system_path import XFileSystemPath


class XText:
    def __init__(self, path: XFileSystemPath):
        self.path = path

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        return self
