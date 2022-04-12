from shared.Domain.x_file_system_path import XFileSystemPath


class XFolder:
    def __init__(self, base_path: XFileSystemPath, folder_name: str):
        self.base_path = base_path
        self.folder_name = folder_name

    def get_base_path(self):
        return self.base_path

    def set_base_path(self, base_path):
        self.base_path = base_path
        return self

    def get_folder_name(self):
        return self.folder_name

    def set_folder_name(self, folder_name):
        self.folder_name = folder_name
        return self

    def get_folder_path(self):
        return self.base_path.of_text() + self.folder_name
