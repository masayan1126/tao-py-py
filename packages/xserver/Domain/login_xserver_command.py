from dataclasses import dataclass
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Core.command import Command
from shared.Core.reciver import Receiver


@dataclass
class LoginXserverCommand(Command):
    web_browser_operator: WebBrowserOperator

    def set_reciver(self, receiver: Receiver):
        self.reciver = receiver

    def execute(self) -> None:
        self.reciver.action(self.web_browser_operator)
