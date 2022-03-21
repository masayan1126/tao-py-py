import os
import pytest
from packages.make_folder.Domain.make_folder_command import MakeFolderCommand
from packages.make_folder.Domain.make_folder_reciver import MakeFolderReciver

from shared.Domain.xfolder import XFolder
from shared.i_command import ICommand


@pytest.fixture
def setuped_basepath():
    return ".\\tests\\"


def test_フォルダを作成できる(setuped_basepath: str) -> None:

    make_folder_command: ICommand = MakeFolderCommand()
    make_folder_command.setReciver(MakeFolderReciver())
    make_folder_command.execute(XFolder(setuped_basepath, "hoge_dir"))

    assert os.path.exists(setuped_basepath + "hoge_dir") == True
