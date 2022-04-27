from shared.Domain.Image.x_image import XImage


class CheckIsBase64Service:
    def check(self, ximage: XImage) -> bool:
        return "base64" in ximage.x_file().x_url().href()
