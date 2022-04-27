from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Image.x_image import XImage
import io
import requests
from PIL import Image
from PIL import UnidentifiedImageError


class ImageDownloader:
    def download(self, x_image: XImage, download_path_to: XFileSystemPath, prefix=None):
        # prefixは連番等を付与してファイル名がフォルダ内で重複しないようにするため
        image_binary = io.BytesIO(requests.get(x_image.x_file().x_url().href()).content)

        try:
            image = Image.open(image_binary)
            image.save(f"{download_path_to.of_text()}/{x_image.x_file().filename()}")

        except UnidentifiedImageError:
            raise UnidentifiedImageError

        # TODO:base64のパターン(base64の形式の場合はdecodeしてDLするか、src属性以外のdata-src等から取得するか)
        # CheckIsBase64Service
        # image_binary = io.BytesIO(base64.b64decode(x_image.get_src().split('base64,')[1]))
        # print(image.copy())

        # TODO: 相対パスの場合
        # if os.path.isabs(x_image.get_src()):
