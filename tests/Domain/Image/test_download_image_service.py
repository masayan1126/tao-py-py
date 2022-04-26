from PIL import UnidentifiedImageError
import pytest
from shared.Application.download_image_service import DownloadImageService
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Image.ximage import XImage
from shared.Domain.xstr import XStr
from shared.Domain.Url.x_url import XUrl


@pytest.fixture
def setuped_ximage() -> None:
    x_url = XUrl(
        encoded_href="https://www.olympus-imaging.jp/product/dslr/e30/sample/images/index_image_02_l.jpg"
    )
    x_image = XImage(x_url=x_url, alt="猫の画像")
    yield x_image
    x_file_system_path = XFileSystemPath(XStr("tests"))
    downloaded_file_path = x_file_system_path.join(x_image.get_file_name())
    downloaded_file_path.delete()


def test_画像をダウンロードできること(setuped_ximage: XImage):

    download_path = XFileSystemPath(XStr("tests")).to_absolute()
    DownloadImageService().download(
        x_image=setuped_ximage, download_path_to=download_path
    )

    assert download_path.exsits()


# def test_識別不可能な画像の場合は例外():
#     with pytest.raises(UnidentifiedImageError):
#         wrong_image_url = "https://www.olympus-imaging.jp/hoge.jpg"
#         x_image = XImage(x_url=XUrl(href=wrong_image_url), alt="")
#         x_file_system_path = XFileSystemPath(XStr("tests"))
#         download_path_to = x_file_system_path.join(x_image.get_file_name())
#         DownloadImageService().download(
#             x_image=x_image, download_path_to=download_path_to
#         )
