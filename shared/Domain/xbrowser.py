from shared.Domain.xdriver import XDriver
from shared.Domain.xurl import XUrl


class XBrowser:
    def __init__(self, xdriver: XDriver, xurl: XUrl):
        self.xurl = xurl
        self.xdriver = xdriver

    def get_url(self):
        return self.xurl.get_href()

    def set_url(self, xurl: XUrl):
        self.xurl = xurl
        return self

    def get_webdriver(self):
        return self.xdriver.get_driver()
