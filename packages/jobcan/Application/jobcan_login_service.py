from packages.jobcan.Domain.login_command import LoginCommand
from packages.jobcan.Domain.login_reciver import LoginReciver
from shared.Application.Init.initializer import Initializer
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.Domain.Scraping.xbrowser import XBrowser
from shared.Domain.xurl import XUrl
from shared.Enums.browser_type import BrowserType
from shared.di_container import DiContainer
from shared.i_command import ICommand


class JobcanLoginService:
    def handle(self):
        Initializer().ioOption()
        xdriver = XDriverFactory().create(BrowserType.CHROME, is_headless=False)
        xbrowser = XBrowserFactory().create(xdriver, XUrl("https://id.jobcan.jp/"))
        web_browser_operator: IWebBrowserOperator = DiContainer().resolve(
            IWebBrowserOperator
        )
        xbrowser: XBrowser = web_browser_operator.boot(xbrowser)

        command: ICommand = LoginCommand(web_browser_operator)
        command.set_reciver(LoginReciver())
        command.execute()

        # 新しいタブに切り替える
        xbrowser.webdriver().switch_to.window(xbrowser.webdriver().window_handles[-1])
        xbrowser.webdriver().get("https://ssl.jobcan.jp/employee/man-hour-manage")

        return web_browser_operator
