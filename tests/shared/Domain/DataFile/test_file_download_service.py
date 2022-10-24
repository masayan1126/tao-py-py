from unittest.mock import MagicMock, patch
import pytest
from shared.Domain.DataFile.file_download_service import FileDownloadService
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.Url.x_url import XUrl
from shared.Domain.DataFile.x_file import XFile


@pytest.fixture
def setuped_xfile() -> None:
    x_url = XUrl(encoded_href="https://www.home-movie.biz/mov/hts-samp001.mp4")
    x_file = XFile(x_url)
    yield x_file


@patch("shared.Domain.DataFile.file_download_service.urllib.request.urlretrieve")
def test_WEB上のファイルをダウンロードできる(mock_urlretrieve_method, setuped_xfile: XFile) -> None:

    mock_urlretrieve_method.return_value = [
        "hoge/foo/var",
        MagicMock(),  # HTTPMessageMock
    ]

    x_file_system_path = XFileSystemPath(XStr("tests"))
    download_path_to = x_file_system_path.to_absolute()

    expected = "hoge/foo/var"
    actual = FileDownloadService().download(
        x_file=setuped_xfile, download_path_to=download_path_to
    )

    assert expected == actual
