from time import sleep
from packages.xserver.Application.open_xserver_filemanager_usecase import (
    OpenXserverFilemanagerUsecase,
)
from shared.Application.Scraping.boot_up_chrome_browser_usecase import (
    BootUpChromeBrowserUsecase,
)
from shared.Domain.Automatic.automatic_operator import AutomaticOperator
from shared.Domain.Automatic.automatic_operator_impl import AutomaticOperatorImpl
from shared.Domain.Url.x_url import XUrl
from packages.xserver.Domain.login_xserver_reciver import LoginXserverReciver
from packages.xserver.Domain.login_xserver_command import LoginXserverCommand
from shared.command import Command


web_browser_operator = BootUpChromeBrowserUsecase(
    x_url=XUrl("https://secure.xserver.ne.jp/xapanel/login/xserver/"),
    is_headless=False,
).handle()

command: Command = LoginXserverCommand(web_browser_operator)
command.set_reciver(LoginXserverReciver())

sleep(3)

automatic_operator: AutomaticOperator = AutomaticOperatorImpl()
OpenXserverFilemanagerUsecase(
    automatic_operator, web_browser_operator, command
).open_filemanager()
