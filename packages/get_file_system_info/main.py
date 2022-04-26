import pandas as pd
from shared.Application.get_file_system_info_service import GetFileSystemInfoService
from shared.Domain.Excel.xcsv import XCsv
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.xstr import XStr


files = GetFileSystemInfoService().get_info(XFileSystemPath("shared", "Application"))

# XCsv().output(
#     XFileSystemPath.home_dir().join("Desktop/path_lists.csv"),
#     pd.DataFrame(data=files),
# )

for root, dirs, files in files:
    print("-" * 10)
    print("root:{}".format(root))
    print("dirs:{}".format(dirs))
    print("files:{}".format(files))

print("debug")
