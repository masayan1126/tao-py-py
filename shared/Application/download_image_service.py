from shared.Application.check_is_valid_url_service import CheckIsValidUrlService
from shared.Domain.ximage import XImage
import io
import requests
from PIL import Image


class DownloadImageService:
    def execute(self, x_image: XImage, download_path_to):

        if not CheckIsValidUrlService().execute(x_image.get_url()):
            return False

        image_binary = io.BytesIO(requests.get(x_image.get_src()).content)
        image = Image.open(image_binary)
        image.save(f"{download_path_to}{x_image.get_file_name()}")

        return f"{download_path_to}{x_image.get_file_name()}"

        # TODO:base64のパターン(base64の形式の場合はdecodeしてDLするか、src属性以外のdata-src等から取得するか)
        # CheckIsBase64Service
        # image_binary = io.BytesIO(base64.b64decode(x_image.get_src().split('base64,')[1]))
        # print(image.copy())

        # TODO: 相対パスの場合
        # if os.path.isabs(x_image.get_src()):
