from dataclasses import dataclass
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.command import Command
from shared.i_reciver import IReceiver


@dataclass
class LoginXserverCommand(Command):
    web_browser_operator: IWebBrowserOperator

    def set_reciver(self, receiver: IReceiver):
        self.reciver = receiver

    def execute(self) -> None:
        self.reciver.action(self.web_browser_operator)
