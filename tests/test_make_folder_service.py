import os

from shared.Application.make_folder_service import MakeFolderService
from shared.Domain.xfolder import XFolder


def test_任意のフォルダを作成できること():

    making_folder_list = ["a", "b", "c\\c-1"]
    base_path = "C:\\Users\\nishigaki\\Desktop\\test\\"

    for folder in making_folder_list:
        x_folder = XFolder(base_path=base_path, folder_name=folder)
        MakeFolderService().execute(x_folder)
        assert os.path.exists(base_path + folder) == True
