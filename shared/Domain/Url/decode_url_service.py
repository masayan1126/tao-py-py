import urllib.parse

from shared.Domain.Url.x_url import XUrl
import urllib.error

# エスケープされた %xx をそれに対応した単一文字に置き換え


class DecodeUrlService:
    def decode(self, xurl: XUrl) -> str:

        try:
            return urllib.parse.unquote(xurl.href())
        except urllib.error.HTTPError as e:
            raise e
