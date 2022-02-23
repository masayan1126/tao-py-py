import pandas as pd
from shared.Application.get_file_system_info_service import GetFileSystemInfoService
from shared.Domain.xcsv import XCsv
from shared.Domain.xpath import XPath


files = GetFileSystemInfoService().execute(
    XPath("C:\\Users\\nishigaki\\jupyter-lab\\shared\\Application")
)

# XCsv().output(
#     "C:\\Users\\nishigaki\\Desktop\\path_lists.csv",
#     pd.DataFrame(data=files),
# )

for root, dirs, files in files:
    print("-" * 10)
    print("root:{}".format(root))
    print("dirs:{}".format(dirs))
    print("files:{}".format(files))
