from shared.Core.factory import Factory
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.TextFile.text_file_operator import TextFileOperator
from shared.Domain.TextFile.text_file_operator_impl import TextFileOperatorImpl


class TextFileOperatorFactory(Factory):
    def create(self, file_path: XFileSystemPath) -> TextFileOperator:
        return TextFileOperatorImpl(file_path)
