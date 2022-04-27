import os
import pytest
from shared.Domain.FileSystem.Command.make_folder_command import MakeFolderCommand
from shared.Domain.FileSystem.make_folder_reciver import MakeFolderReciver
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath

from shared.Domain.FileSystem.x_folder import XFolder
from shared.Domain.String.xstr import XStr
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
