from shared.Core.factory import Factory
from shared.Domain.Scraping.xbrowser import XBrowser
from shared.Domain.Scraping.xdriver import XDriver
from shared.Domain.Url.x_url import XUrl


class XBrowserFactory(Factory):
    def create(self, xdriver: XDriver, xurl: XUrl) -> XBrowser:
        return XBrowser(xdriver, xurl)
