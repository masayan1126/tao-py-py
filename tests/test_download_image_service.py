from shared.Application.download_image_service import DownloadImageService
from shared.Domain.ximage import XImage
from shared.Domain.xurl import XUrl
import os


def test_画像をダウンロードできること():

    image_url = "https://www.olympus-imaging.jp/product/dslr/e30/sample/images/index_image_02_l.jpg"

    x_url = XUrl(href=image_url)

    x_image = XImage(x_url=x_url, alt="猫の画像")
    download_path_to = "C:\\Users\\nishigaki\\Desktop\\"
    downloaded_image_filepath = DownloadImageService().execute(
        x_image=x_image, download_path_to=download_path_to
    )

    assert os.path.isfile(downloaded_image_filepath) == True


def test_無効なURLを渡すとFalseが返ること():

    image_url = "https://www.olympus-imaging.jp/hoge.jpg"

    x_url = XUrl(href=image_url)

    x_image = XImage(x_url=x_url, alt="猫の画像")
    download_path_to = "C:\\Users\\nishigaki\\Desktop\\"
    downloaded_image_filepath = DownloadImageService().execute(
        x_image=x_image, download_path_to=download_path_to
    )

    assert downloaded_image_filepath == False
