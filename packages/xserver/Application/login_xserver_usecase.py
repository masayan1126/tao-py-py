from time import sleep
from packages.twi_automation.env import ENV
from packages.xserver.Application.login_xserver_reciver import LoginXserverReciver
from shared.Application.Scraping.boot_up_chrome_browser_usecase import (
    BootUpChromeBrowserUsecase,
)
from shared.Domain.Log.x_logger import XLogger
from shared.Domain.Scraping.Command.login_command import LoginCommand
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Url.x_url import XUrl
from shared.i_command import ICommand
from selenium.common.exceptions import SessionNotCreatedException


class LoginXserverUsecase:
    def login(self) -> IWebBrowserOperator:
        try:
            web_browser_operator = BootUpChromeBrowserUsecase(
                x_url=XUrl("https://secure.xserver.ne.jp/xapanel/login/xserver/"),
                is_headless=False,
            ).handle()

            command: ICommand = LoginCommand(web_browser_operator)
            command.set_reciver(LoginXserverReciver())
            command.execute()

            sleep(2)
            # # 新しいタブに切り替える
            web_browser_operator.webdriver().switch_to.window(
                web_browser_operator.webdriver().window_handles[-1]
            )

            btn = web_browser_operator.find_by_xpath(
                "/html/body/main/div/section[1]/table/tbody/tr[2]/td[6]/a[1]"
            )
            btn.web_element().click()

            return web_browser_operator

        except SessionNotCreatedException as e:
            XLogger.exception_to_slack(
                ENV["SLACK_WEBHOOK_URL_COMMON"],
                "Chromeブラウザーのバージョンが最新でない可能性があります。一度確認してみてください",
            )
            raise e
