from shared.Domain.DataFile.Excel.excel_file_operator_impl import ExcelFileOperatorImpl
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr

# memo: 現状、csvで足りているので、一旦保留とする

filepath = XFileSystemPath(XStr("packages/open_excel/sample.xlsx")).to_absolute()
xworkbook = ExcelFileOperatorImpl().read(filepath, sheet_name=None)
xworksheet = xworkbook.get_sheet_by_name("プログラミング言語一覧")
target_cell_records = xworksheet.get_records(0, 100, 0, 6)
