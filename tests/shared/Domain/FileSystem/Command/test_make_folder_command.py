import pytest
from shared.Domain.FileSystem.make_folder_command import MakeFolderCommand
from shared.Domain.FileSystem.make_folder_reciver import MakeFolderReciver
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath

from shared.Domain.FileSystem.x_folder import XFolder
from shared.Domain.String.xstr import XStr
from shared.Core.command import Command


@pytest.fixture
def sut():
    sut: Command = MakeFolderCommand()
    sut.set_reciver(MakeFolderReciver())
    yield sut
    XFileSystemPath(XStr("tests/sample")).to_absolute().delete()


def test_フォルダを作成できる(sut: Command) -> None:
    filepath = XFileSystemPath(XStr("tests/sample")).to_absolute()
    sut.execute(XFolder(filepath))

    assert filepath.exsits()
