import pytest
import os
from shared.Application.download_file_service import DownloadFileService
from shared.Domain.x_file_system_path import XFileSystemPath
from shared.Domain.xstr import XStr
from shared.Domain.xurl import XUrl
from shared.Domain.xfile import XFile


@pytest.fixture
def setuped_xfile() -> None:
    x_url = XUrl(href="https://www.home-movie.biz/mov/hts-samp001.mp4")
    x_file = XFile(x_url)
    yield x_file
    x_file_system_path = XFileSystemPath(XStr("tests"))
    downloaded_file_path = x_file_system_path.join(x_file.get_file_name())
    downloaded_file_path.delete()


def test_任意のファイルをダウンロードできること(setuped_xfile: XFile) -> None:

    x_file_system_path = XFileSystemPath(XStr("tests"))
    download_path_to = x_file_system_path.to_absolute()

    DownloadFileService().download(
        x_file=setuped_xfile, download_path_to=download_path_to, extension=".mp4"
    )

    downloaded_file_path = x_file_system_path.join(setuped_xfile.get_file_name())

    assert downloaded_file_path.exsits()
