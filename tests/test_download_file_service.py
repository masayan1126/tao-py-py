import pytest
import os
from shared.Application.download_file_service import DownloadFileService
from shared.Domain.xurl import XUrl
from shared.Domain.xfile import XFile


@pytest.fixture
def setuped_xfile() -> None:
    x_url = XUrl(href="https://www.home-movie.biz/mov/hts-samp001.mp4")
    x_file = XFile(x_url)
    return x_file


def test_任意のファイルをダウンロードできること(setuped_xfile: XFile) -> None:

    download_path_to = "C:\\Users\\nishigaki\\Desktop\\"

    DownloadFileService().download(
        x_file=setuped_xfile, download_path_to=download_path_to, extension=".mp4"
    )

    assert os.path.isfile("C:\\Users\\nishigaki\\Desktop\\hts-samp001.mp4")
