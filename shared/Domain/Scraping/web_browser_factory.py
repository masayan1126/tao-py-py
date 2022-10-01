from shared.Core.di_container import DiContainer
from shared.Core.factory import Factory
from shared.Domain.Log.x_logger import XLogger
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.Domain.Url.x_url import XUrl
from shared.Enums.browser_type import BrowserType


class WebBrowserFactory(Factory):
    def create(
        self, browser_type: BrowserType, x_url: XUrl, is_headless=True, on_docker=False
    ) -> WebBrowserOperator:

        xdriver = XDriverFactory().create(
            browser_type, is_headless=is_headless, on_docker=on_docker
        )

        xbrowser = XBrowserFactory().create(xdriver, x_url)

        web_browser_operator: WebBrowserOperator = DiContainer().resolve(
            WebBrowserOperator
        )

        web_browser_operator.boot(xbrowser)

        return web_browser_operator
