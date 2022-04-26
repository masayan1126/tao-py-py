from shared.i_factory import IFactory
from shared.Domain.Scraping.xbrowser import XBrowser
from shared.Domain.Scraping.xdriver import XDriver
from shared.Domain.Url.x_url import XUrl


class XBrowserFactory(IFactory):
    def create(self, xdriver: XDriver, xurl: XUrl) -> XBrowser:
        return XBrowser(xdriver, xurl)
