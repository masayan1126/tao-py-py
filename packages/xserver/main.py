from time import sleep
from packages.xserver.Application.open_xserver_filemanager_usecase import (
    OpenXserverFilemanagerUsecase,
)

from shared.Domain.Automatic.automatic_operator import AutomaticOperator
from shared.Domain.Automatic.automatic_operator_impl import AutomaticOperatorImpl
from shared.Domain.Scraping.web_browser_factory import WebBrowserFactory
from shared.Domain.Url.x_url import XUrl
from packages.xserver.Domain.login_xserver_reciver import LoginXserverReciver
from packages.xserver.Domain.login_xserver_command import LoginXserverCommand
from shared.Core.command import Command
from shared.Domain.Scraping.browser_type import BrowserType


chrome_browser_operator = WebBrowserFactory().create(
    XUrl("https://secure.xserver.ne.jp/xapanel/login/xserver/"),
    BrowserType.CHROME,
    is_headless=False,
)

command: Command = LoginXserverCommand(chrome_browser_operator)
command.set_reciver(LoginXserverReciver())

sleep(3)

automatic_operator: AutomaticOperator = AutomaticOperatorImpl()
OpenXserverFilemanagerUsecase(
    automatic_operator, chrome_browser_operator, command
).open_filemanager()
