import os

from shared.Domain.x_file_system_path import XFileSystemPath


# 対象のディレクトリに存在するディレクトリ名とファイル名を返します
class GetFileSystemInfoService:
    def get_info(self, x_file_system_path: XFileSystemPath):
        return os.walk(x_file_system_path.abs_path())
