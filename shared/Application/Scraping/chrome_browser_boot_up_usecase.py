from shared.Domain.Log.x_logger import XLogger
from shared.Domain.Scraping.web_browser_factory import WebBrowserFactory
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.Domain.Url.x_url import XUrl
from shared.Enums.browser_type import BrowserType
from shared.Core.di_container import DiContainer
from packages.jobcan.env import ENV as ENV_JOBCAN


class ChromeBrowserBootUpUsecase:
    def __init__(self, x_url: XUrl, is_headless=False) -> None:
        self.x_url = x_url
        self.is_headless = is_headless

    def handle(self) -> WebBrowserOperator:
        # xdriver = XDriverFactory().create(
        #     browser_type=BrowserType.CHROME, is_headless=self.is_headless
        # )
        # xbrowser = XBrowserFactory().create(xdriver, self.x_url)
        # web_browser_operator: WebBrowserOperator = DiContainer().resolve(
        #     WebBrowserOperator
        # )
        # web_browser_operator.boot(xbrowser)

        # print(
        #     {
        #         "aaa": WebBrowserFactory().create(
        #             BrowserType.CHROME, self.x_url, self.is_headless
        #         )
        #     }
        # )

        XLogger.notification_to_slack(
            ENV_JOBCAN["SLACK_WEBHOOK_URL_JOBCAN"],
            WebBrowserFactory().create(
                BrowserType.CHROME, self.x_url, self.is_headless
            ),
        )

        return WebBrowserFactory().create(
            BrowserType.CHROME, self.x_url, self.is_headless
        )
