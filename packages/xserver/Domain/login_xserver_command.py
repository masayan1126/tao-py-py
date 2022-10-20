from dataclasses import dataclass
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Core.command import Command
from shared.Core.i_reciver import IReceiver


@dataclass
class LoginXserverCommand(Command):
    web_browser_operator: WebBrowserOperator

    def set_reciver(self, receiver: IReceiver):
        self.reciver = receiver

    def execute(self) -> None:
        self.reciver.action(self.web_browser_operator)
