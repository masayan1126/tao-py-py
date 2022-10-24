from __future__ import annotations
from abc import ABCMeta, abstractmethod
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath


class DataFileOperator(metaclass=ABCMeta):
    @abstractmethod
    def read(self, filepath: XFileSystemPath) -> list:
        pass

    @abstractmethod
    def output(self, filepath: XFileSystemPath, data_list: list) -> None:
        pass
