from selenium import webdriver
from shared.Application.Init.initializer import Initializer
from shared.i_factory import IFactory
from shared.Domain.browser_factory import BrowserFactory
from shared.di_container import DiContainer
from shared.Domain.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.xbrowser import XBrowser
from shared.Domain.xurl import XUrl
from shared.Domain.xweb_element import XWebElement
from shared.Domain.xweb_element_list import XWebElementList
from shared.Enums.browser_type import BrowserType
from time import sleep
import os


# 1.初期化
Initializer().ioOption()
xdriver = Initializer().webBrowserOption(BrowserType.CHROME, is_headless=False)
i_web_browser_operator: IWebBrowserOperator = DiContainer().resolve(IWebBrowserOperator)


# 2.ブラウザ起動 ---------------------------------------------------------------------------------------------------
factory: IFactory = BrowserFactory()
xbrowser = factory.create(xdriver, XUrl("https://id.jobcan.jp/"))
i_web_browser_operator.boot(xbrowser)


# 3.htmlを取得し値をセットして送信 -----------------------------------------------------------------------------------
# TODO:返り値はXwebelemtnになるように
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
i_web_browser_operator.find_by_xpath(xpath="//*[@id='new_user']/input[2]").click()

sleep(1)

i_web_browser_operator.find_by_xpath(
    xpath="//*[@id='jbc-app-links']/ul/li[2]/a"
).click()
