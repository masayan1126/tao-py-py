from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.i_command import ICommand
from shared.i_reciver import IReceiver


class LoginCommand(ICommand):
    def __init__(self, i_web_browser_operator: IWebBrowserOperator):
        self.i_web_browser_operator = i_web_browser_operator

    def set_reciver(self, receiver: IReceiver):
        self.reciver = receiver

    def execute(self) -> None:
        self.reciver.action(self.i_web_browser_operator)
