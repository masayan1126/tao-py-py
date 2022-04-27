from packages.jobcan.Domain.Command.login_command import LoginCommand
from packages.jobcan.Application.login_reciver import LoginReciver
from packages.twi_automation.env import ENV
from shared.Application.Init.initializer import Initializer
from shared.Application.Scraping.boot_up_chrome_browser_usecase import (
    BootUpChromeBrowserUsecase,
)
from shared.Domain.Log.x_logger import XLogger
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.Domain.Scraping.xbrowser import XBrowser
from shared.Domain.Url.x_url import XUrl
from shared.Enums.browser_type import BrowserType
from shared.di_container import DiContainer
from shared.i_command import ICommand
from selenium.common.exceptions import SessionNotCreatedException


class LoginJobcanUsecase:
    def handle(self) -> IWebBrowserOperator:
        try:
            web_browser_operator = BootUpChromeBrowserUsecase(
                x_url=XUrl("https://id.jobcan.jp/"), is_headless=False
            ).handle()

            command: ICommand = LoginCommand(web_browser_operator)
            command.set_reciver(LoginReciver())
            command.execute()

            # 新しいタブに切り替える
            web_browser_operator.webdriver().switch_to.window(
                web_browser_operator.webdriver().window_handles[-1]
            )
            web_browser_operator.webdriver().get(
                "https://ssl.jobcan.jp/employee/man-hour-manage"
            )

            return web_browser_operator

        except SessionNotCreatedException as e:
            XLogger.exception_to_slack(
                ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
                "Chromeブラウザーのバージョンが最新でない可能性があります。一度確認してみてください",
            )
            raise e
