from shared.Domain.Url.x_url import XUrl
import urllib.parse


class EncoderUrlService:
    def encode(self, xurl: XUrl, not_escape_ascii="/") -> str:
        return urllib.parse.quote(xurl.href(), safe=not_escape_ascii)
