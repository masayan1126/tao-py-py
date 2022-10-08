from dataclasses import dataclass
from time import sleep
from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Domain.Automatic.automatic_operator import AutomaticOperator
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Core.command import Command
from packages.xserver.env import ENV
from selenium.common.exceptions import SessionNotCreatedException


@dataclass
class OpenXserverFilemanagerUsecase:
    automatic_operator: AutomaticOperator
    web_browser_operator: WebBrowserOperator
    login_xserver_command: Command

    def open_filemanager(self):
        try:
            self.login_xserver_command.execute()
            sleep(2)

            self.web_browser_operator.switch_new_tab()

            btn_to_filemanager = self.web_browser_operator.find_by_xpath(
                "/html/body/main/div/section[1]/table/tbody/tr[2]/td[6]/a[1]"
            )
            btn_to_filemanager.click()
            sleep(2)

            self.automatic_operator.click(x=127, y=466, duration=1, wait_time=1).click(
                x=163, y=623, duration=1, wait_time=1
            ).click(x=124, y=759, duration=1, wait_time=1).click(
                x=161, y=811, duration=1, wait_time=1
            ).click(
                x=201, y=904, duration=1, wait_time=1
            )

        except SessionNotCreatedException:
            LogHandler(
                LogType.EXCEPTION,
                "Browser version may not be up to date .",
            ).to_slack(ENV["SLACK_WEBHOOK_URL_COMMON"])
