from shared.Domain.Scraping.xdriver import XDriver
from shared.Domain.xurl import XUrl


class XBrowser:
    def __init__(self, xdriver: XDriver, xurl: XUrl):
        self.xurl = xurl
        self.xdriver = xdriver

    def url(self):
        return self.xurl.get_href()

    def webdriver(self):
        return self.xdriver.driver()
