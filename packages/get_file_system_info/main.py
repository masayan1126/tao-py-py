import pandas as pd
from shared.Application.get_file_system_info_service import GetFileSystemInfoService
from shared.Domain.xcsv import XCsv
from shared.Domain.xpath import XPath


files = GetFileSystemInfoService().execute(
    XPath("C:\\Users\\nishigaki\\Desktop\\tavenal-com\\public\\comm")
)

# print(files)

# for f in files:
#     print(f)

XCsv().output(
    "C:\\Users\\nishigaki\\Desktop\\path_list.csv",
    pd.DataFrame(data=files, columns={"ファイル名", "a", "b"}),
)
