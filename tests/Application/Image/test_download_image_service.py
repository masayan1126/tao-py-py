import pytest
from shared.Domain.File.x_file import XFile
from shared.Domain.Image.image_downloader import ImageDownloader
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Image.x_image import XImage
from shared.Domain.String.xstr import XStr
from shared.Domain.Url.x_url import XUrl


@pytest.fixture
def setuped_x_image() -> None:
    x_url = XUrl(
        encoded_href="https://www.olympus-imaging.jp/product/dslr/e30/sample/images/index_image_02_l.jpg"
    )
    x_image = XImage(x_file=XFile(x_url))
    yield x_image
    x_file_system_path = XFileSystemPath(XStr("tests"))
    downloaded_file_path = x_file_system_path.join(x_image.x_file().filename())
    downloaded_file_path.delete()


def test_画像をダウンロードできること(setuped_x_image: XImage) -> None:

    download_path_to = XFileSystemPath(XStr("tests")).to_absolute()
    ImageDownloader().download(
        x_image=setuped_x_image, download_path_to=download_path_to
    )

    assert download_path_to.exsits()
