import urllib.parse

from shared.Domain.xurl import XUrl

# エスケープされた %xx をそれに対応した単一文字に置き換え
class DecodeUrlService:
    def execute(self, xurl: XUrl) -> str:
        return urllib.parse.unquote(xurl.get_href())
