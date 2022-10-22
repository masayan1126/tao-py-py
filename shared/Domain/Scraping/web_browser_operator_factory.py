from shared.Core.di_container import DiContainer
from shared.Core.factory import Factory
from shared.Domain.Scraping.browser_driver_type_judgement import (
    BrowserDriverTypeJudgement,
)
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.Url.x_url import XUrl
from shared.Domain.Scraping.browser_type import BrowserType
from selenium.webdriver.remote.webdriver import WebDriver


class WebBrowserOperatorFactory(Factory):
    def create(
        self,
        x_url: XUrl,
        browser_type: BrowserType = BrowserType.CHROME,
        is_headless=True,
    ) -> WebBrowserOperator:

        judgement = BrowserDriverTypeJudgement(browser_type, is_headless)
        webdriver: WebDriver = judgement.judge()

        web_browser_operator: WebBrowserOperator = DiContainer().resolve(
            WebBrowserOperator
        )

        web_browser_operator.boot(webdriver, x_url)

        return web_browser_operator
