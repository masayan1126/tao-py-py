import io, sys
from packages.make_folder.Application.folder_make_usecase import FolderMakeUsecase
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

FolderMakeUsecase(
    XFileSystemPath(XStr("packages/make_folder/list.csv")).to_absolute()
).make()
