from shared.Application.Init.initializer import Initializer
from shared.di_container import DiContainer
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.Domain.xurl import XUrl
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.Enums.browser_type import BrowserType
from shared.i_factory import IFactory
from time import sleep
import os


Initializer().ioOption()

# 1.ブラウザ起動 ---------------------------------------------------------------------------------------------------
factory: IFactory = XDriverFactory()
xdriver = factory.create(BrowserType.CHROME, is_headless=False)
factory: IFactory = XBrowserFactory()
xbrowser = factory.create(xdriver, XUrl("https://id.jobcan.jp/"))
i_web_browser_operator: IWebBrowserOperator = DiContainer().resolve(IWebBrowserOperator)
i_web_browser_operator.boot(xbrowser)


# 2.htmlを取得し値をセットして送信 -----------------------------------------------------------------------------------
user_email = i_web_browser_operator.find_by_id(id_name="user_email")
user_password = i_web_browser_operator.find_by_id(id_name="user_password")

i_web_browser_operator.send_value(
    XWebElementList(
        [
            user_email.set_value(os.environ.get("AIVICK_EMAIL")),
            user_password.set_value(os.environ.get("JOBCAN_PASSWORD")),
        ]
    )
)
i_web_browser_operator.find_by_xpath(
    xpath="//*[@id='new_user']/input[2]"
).web_element().click()

sleep(1)

i_web_browser_operator.find_by_xpath(
    xpath="//*[@id='jbc-app-links']/ul/li[2]/a"
).web_element().click()
