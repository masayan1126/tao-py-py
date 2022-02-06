from shared.Domain.ximage import XImage

class CheckIsBase64Service:
    def execute(self,ximage:XImage):
        return "base64" in ximage.get_src()