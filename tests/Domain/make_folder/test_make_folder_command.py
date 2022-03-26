import os
import pytest
from packages.make_folder.Domain.make_folder_command import MakeFolderCommand
from packages.make_folder.Domain.make_folder_reciver import MakeFolderReciver

from shared.Domain.xfolder import XFolder
from shared.i_command import ICommand


@pytest.fixture
def setuped_command():
    command: ICommand = MakeFolderCommand()
    command.set_reciver(MakeFolderReciver())
    return command


def test_フォルダを作成できる(setuped_command: ICommand) -> None:
    basepath = ".\\tests\\"
    setuped_command.execute(XFolder(basepath, "hoge_dir"))

    assert os.path.exists(basepath + "hoge_dir")
