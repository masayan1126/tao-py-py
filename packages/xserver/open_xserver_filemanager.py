from time import sleep
from packages.xserver.Application.xserver_filemanager_open_usecase import (
    XserverFilemanagerOpenUsecase,
)

from shared.Domain.GUI.gui_operator_impl import GUIOperatorImpl
from shared.Domain.Scraping.web_browser_operator_factory import (
    WebBrowserOperatorFactory,
)
from shared.Domain.Url.x_url import XUrl
from packages.xserver.Command.login_xserver_reciver import LoginXserverReciver
from packages.xserver.Command.login_xserver_command import LoginXserverCommand
from shared.Domain.Scraping.browser_type import BrowserType


chrome_browser_operator = WebBrowserOperatorFactory().create(
    XUrl("https://secure.xserver.ne.jp/xapanel/login/xserver/"),
    BrowserType.CHROME,
)

command = LoginXserverCommand()
command.set_reciver(LoginXserverReciver(chrome_browser_operator))

sleep(3)

XserverFilemanagerOpenUsecase(
    GUIOperatorImpl(), chrome_browser_operator, command
).open()
