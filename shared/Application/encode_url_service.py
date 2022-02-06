from shared.Domain.xurl import XUrl
from shared.Domain.ximage import XImage
import urllib.parse

# 特殊文字を%エスケープを使った文字に置き換え
class EncodeUrlService:
    def execute(self, xurl: XUrl, not_escape_ascii="/"):
        return urllib.parse.quote(xurl.get_href(), safe=not_escape_ascii)
