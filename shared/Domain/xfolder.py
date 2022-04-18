from shared.Domain.x_file_system_path import XFileSystemPath


class XFolder:
    def __init__(self, base_path: XFileSystemPath):
        self.base_path = base_path

    def get_base_path(self):
        return self.base_path

    def set_base_path(self, base_path):
        self.base_path = base_path
        return self

    def get_folder_name(self):
        return self.base_path.to_relative().of_text()

    def get_folder_path(self):
        return self.base_path.of_text()
