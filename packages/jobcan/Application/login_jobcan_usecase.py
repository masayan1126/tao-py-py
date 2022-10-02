from packages.jobcan.Application.login_reciver import LoginReciver
from packages.jobcan.env import ENV

from shared.Domain.Log.x_logger import XLogger
from packages.xserver.Domain.login_xserver_command import LoginXserverCommand
from shared.Domain.Scraping.web_browser_factory import WebBrowserFactory
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.Url.x_url import XUrl
from shared.Core.command import Command
from selenium.common.exceptions import SessionNotCreatedException
from shared.Domain.Scraping.browser_type import BrowserType


class LoginJobcanUsecase:
    def handle(self) -> WebBrowserOperator:
        try:

            web_browser_operator = WebBrowserFactory().create(
                BrowserType.CHROME,
                x_url=XUrl("https://id.jobcan.jp/"),
                is_headless=False,
            )

            command: Command = LoginXserverCommand(web_browser_operator)
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
                ENV["SLACK_WEBHOOK_URL_JOBCAN"],
                "Chromeブラウザーのバージョンが最新でない可能性があります。一度確認してみてください",
            )
            raise e
