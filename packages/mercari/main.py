import sys
from packages.mercari.Application.exhibit_new_product_usecase import (
    ExhibitNewProductUsecase,
)
import pyautogui as pgui
import pyperclip
from shared.Domain.Text.text_file_service import TextFileService
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.Text.x_text import XText

# memo: メルカリの新規出品ページを開いた状態でこのスクリプトを実行する

detail = ""
detail_filepath = XFileSystemPath(XStr("packages/mercari/detail.txt")).to_absolute()


ExhibitNewProductUsecase().exhibit(detail_filepath)
