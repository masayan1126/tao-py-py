from shared.Domain.Url.x_url import XUrl
import urllib.parse

# 特殊文字を%エスケープを使った文字に置き換え
class EncoderUrlService:
    def encode(self, xurl: XUrl, not_escape_ascii="/") -> str:
        return urllib.parse.quote(xurl.href(), safe=not_escape_ascii)
