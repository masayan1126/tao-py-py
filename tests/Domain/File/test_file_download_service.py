import pytest
from shared.Domain.File.file_downloade_service import FileDownloadeService
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.Url.x_url import XUrl
from shared.Domain.File.x_file import XFile


@pytest.fixture
def setuped_xfile() -> None:
    x_url = XUrl(encoded_href="https://www.home-movie.biz/mov/hts-samp001.mp4")
    x_file = XFile(x_url)
    yield x_file
    x_file_system_path = XFileSystemPath(XStr("tests"))
    downloaded_file_path = x_file_system_path.join(x_file.filename())
    downloaded_file_path.delete()


def test_任意のファイルをダウンロードできること(setuped_xfile: XFile) -> None:

    x_file_system_path = XFileSystemPath(XStr("tests"))
    download_path_to = x_file_system_path.to_absolute()

    FileDownloadeService().download(
        x_file=setuped_xfile, download_path_to=download_path_to, extension=".mp4"
    )

    downloaded_file_path = x_file_system_path.join(setuped_xfile.filename())

    assert downloaded_file_path.exsits()
