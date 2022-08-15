from packages.mercari.Application.exhibit_new_product_usecase import (
    ExhibitNewProductUsecase,
)
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr

# memo: メルカリの新規出品ページを開いた状態でこのスクリプトを実行する

detail = ""
detail_filepath = XFileSystemPath(XStr("packages/mercari/detail.txt")).to_absolute()


ExhibitNewProductUsecase().exhibit(detail_filepath)
