import io, sys
from packages.make_folder.Application.make_folder_usecase import MakeFolderUsecase
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

MakeFolderUsecase(
    XFileSystemPath(XStr("packages/make_folder/list.csv")).to_absolute()
).make()
