from packages.mercari.Application.new_product_exhibit_usecase import (
    NewProductExhibitUsecase,
)
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr

# memo: メルカリの新規出品ページを開いた状態でこのスクリプトを実行する

detail = ""
detail_filepath = XFileSystemPath(XStr("packages/mercari/detail.txt")).to_absolute()


NewProductExhibitUsecase().exhibit(detail_filepath)
