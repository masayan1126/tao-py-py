import io, sys
from pprint import pprint
from glob import glob
from shared.Domain.xexcel import XExcel

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

filepath = glob("C:\\Users\\nishigaki\\jupyter-lab\\packages\\open_excel\\*.xlsx")[0]
xworkbook = XExcel().read(filepath, sheet_name=None)
xworksheet = xworkbook.get_sheet_by_name("プログラミング言語一覧")
target_cell_records = xworksheet.get_records(0, 100, 0, 6)

for target_cell_record in target_cell_records:
    pprint(target_cell_record)

# the_cell = xworksheet.get_cell(index_number=2, column_number=1)
# print(the_cell)

# pg_lang_series = pd.Series(["PHP", "Java", "Python", "Ruby"])

# data = {
#     "ID": [1, 2, 3, 4],
#     "言語名": ["PHP", "Java", "Python", "Ruby"],
#     "型": ["動的型付け", "静的型付け", "動的型付け", "動的型付け"],
# }

# pg_lang_data_frame = pd.DataFrame(data, columns=["ID", "言語名", "型"])
