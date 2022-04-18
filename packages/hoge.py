import pathlib
from shared.Domain.Excel.xexcel import XExcel

from shared.Domain.x_file_system_path import XFileSystemPath
from shared.Domain.xstr import XStr


filepath = XFileSystemPath(XStr("tests/sample.xlsx")).to_absolute()
xworkbook = XExcel().read(filepath, sheet_name=None, header_row_number=None)
xworksheet = xworkbook.get_sheet_by_name("プログラミング言語一覧")
cell = xworksheet.get_cell(0, 0)

print("debug")
