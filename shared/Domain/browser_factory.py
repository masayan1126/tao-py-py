from shared.i_factory import IFactory
from shared.Domain.xbrowser import XBrowser
from shared.Domain.xdriver import XDriver
from shared.Domain.xurl import XUrl


class BrowserFactory(IFactory):
    def create(self, xdriver: XDriver, xurl: XUrl) -> XBrowser:
        return XBrowser(xdriver, xurl)
