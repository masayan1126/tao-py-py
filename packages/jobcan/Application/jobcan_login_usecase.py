from packages.jobcan.Application.login_reciver import LoginReciver
from packages.jobcan.env import ENV
from packages.xserver.Domain.login_xserver_command import LoginXserverCommand
from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Domain.Scraping.web_browser_factory import WebBrowserFactory
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.Url.x_url import XUrl
from shared.Core.command import Command
from selenium.common.exceptions import SessionNotCreatedException
from shared.Domain.Scraping.browser_type import BrowserType


class JobcanLoginUsecase:
    def handle(self) -> WebBrowserOperator:
        try:

            web_browser_operator = WebBrowserFactory().create(
                x_url=XUrl("https://id.jobcan.jp/"),
                browser_type=BrowserType.CHROME,
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

        except SessionNotCreatedException:
            LogHandler(
                LogType.EXCEPTION,
                "Browser version may not be up to date .",
            ).to_slack(ENV["SLACK_WEBHOOK_URL_JOBCAN"])
