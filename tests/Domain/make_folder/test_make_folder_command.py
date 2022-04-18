import os
import pytest
from packages.make_folder.Domain.make_folder_command import MakeFolderCommand
from packages.make_folder.Domain.make_folder_reciver import MakeFolderReciver
from shared.Domain.x_file_system_path import XFileSystemPath

from shared.Domain.xfolder import XFolder
from shared.Domain.xstr import XStr
from shared.i_command import ICommand


@pytest.fixture
def setuped_command():
    command: ICommand = MakeFolderCommand()
    command.set_reciver(MakeFolderReciver())
    yield command
    XFileSystemPath(XStr("tests/sample")).to_absolute().delete()


def test_フォルダを作成できる(setuped_command: ICommand) -> None:
    filepath = XFileSystemPath(XStr("tests/sample")).to_absolute()
    setuped_command.execute(XFolder(filepath))

    assert filepath.exsits()
