from dataclasses import dataclass
import urllib.parse

from shared.Domain.Url.x_url import XUrl
import urllib.error


@dataclass
class UrlParseService:
    xurl: XUrl

    def decode(self) -> XUrl:
        return XUrl(urllib.parse.unquote(self.xurl.href()))

    def encode(self, not_escape_ascii="/") -> XUrl:
        return XUrl(urllib.parse.quote(self.xurl.href(), safe=not_escape_ascii))
