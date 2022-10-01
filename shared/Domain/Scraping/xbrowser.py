from dataclasses import dataclass
from shared.Domain.Scraping.xdriver import XDriver
from shared.Domain.Url.x_url import XUrl


@dataclass
class XBrowser:
    def __init__(self, xdriver: XDriver, xurl: XUrl):
        self.xurl = xurl
        self._xdriver = xdriver

    def url(self):
        return self.xurl.href()

    def xdriver(self) -> XDriver:
        return self._xdriver
