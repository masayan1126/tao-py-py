from shared.Core.factory import Factory
from shared.Domain.DataFile.Csv.csv_file_operator_impl import CsvFileOperatorImpl
from shared.Domain.DataFile.data_file_operator import DataFileOperator
from shared.Domain.DataFile.Excel.excel_file_operator_impl import ExcelFileOperatorImpl
from shared.Domain.FileSystem.file_format_type import FileFormatType


class DataFileOperatorFactory(Factory):
    def create(
        self,
        file_format_type: FileFormatType,
    ) -> DataFileOperator:

        if file_format_type is FileFormatType.CSV:
            return CsvFileOperatorImpl()
        elif file_format_type is FileFormatType.EXCEL:
            return ExcelFileOperatorImpl()
