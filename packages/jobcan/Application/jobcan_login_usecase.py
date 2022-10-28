from packages.jobcan.Command.login_jobcan_command import LoginJobcanCommand
from packages.jobcan.Command.login_jobcan_reciver import LoginJobcanReciver
from packages.jobcan.env import ENV
from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator


class JobcanLoginUsecase:
    def __init__(self, web_browser_operator: WebBrowserOperator):
        self.web_browser_operator = web_browser_operator

    def login(self) -> None:
        try:
            command = LoginJobcanCommand()
            command.set_reciver(LoginJobcanReciver(self.web_browser_operator))
            command.execute()

        except Exception as e:
            LogHandler(
                LogType.EXCEPTION,
                e,
                ENV["PACKAGE_NAME"],
            ).to_slack(ENV["SLACK_WEBHOOK_URL_JOBCAN"])
