from shared.Core.factory import Factory
from shared.Domain.Scraping.firefox_browser_operator_impl import (
    FirefoxBrowserOperatorImpl,
)
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.Scraping.chrome_browser_operator_impl import (
    ChromeBrowserOperatorImpl,
)
from shared.Domain.Url.x_url import XUrl
from shared.Domain.Scraping.browser_type import BrowserType


class WebBrowserOperatorFactory(Factory):
    def create(
        self,
        x_url: XUrl,
        browser_type: BrowserType = BrowserType.CHROME,
        is_headless=False,
    ) -> WebBrowserOperator:

        if browser_type == BrowserType.CHROME:
            return ChromeBrowserOperatorImpl(x_url, is_headless)
        elif browser_type == BrowserType.FIREFOX:
            return FirefoxBrowserOperatorImpl(x_url, is_headless)
