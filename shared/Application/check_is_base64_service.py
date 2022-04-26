from shared.Domain.Image.ximage import XImage


class CheckIsBase64Service:
    def execute(self, ximage: XImage) -> bool:
        return "base64" in ximage.get_src()
