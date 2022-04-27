from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.Domain.Url.x_url import XUrl
from shared.Enums.browser_type import BrowserType
from shared.di_container import DiContainer
from selenium.common.exceptions import SessionNotCreatedException


class BootUpChromeBrowserUsecase:
    def __init__(self, x_url: XUrl, is_headless=False) -> None:
        self.x_url = x_url
        self.is_headless = is_headless

    def handle(self) -> IWebBrowserOperator:
        try:
            xdriver = XDriverFactory().create(browser_type=BrowserType.CHROME, is_headless=self.is_headless)
            xbrowser = XBrowserFactory().create(xdriver, self.x_url)
            web_browser_operator: IWebBrowserOperator = DiContainer().resolve(
                IWebBrowserOperator
            )
            web_browser_operator.boot(xbrowser)

            return web_browser_operator
        except SessionNotCreatedException as e:
            raise e
