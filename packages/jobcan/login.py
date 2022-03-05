import os
from time import sleep
from selenium import webdriver
from shared.Application.Init.initializer import Initializer
from shared.Application.find_web_elements_service import FindWebElementsService

from shared.Application.open_browser_service import OpenBrowserService
from shared.Application.open_text_service import OpenTextService
from shared.Application.set_webelement_service import SetWebElementService
from shared.Domain.Scraping.selenium_scraper import SeleniumScraper
from shared.Domain.xbrowser import XBrowser
from shared.Domain.xtext import XText
from shared.Domain.xurl import XUrl
from shared.Domain.xweb_element import XWebElement
from shared.Domain.xweb_element_list import XWebElementList
from shared.Enums.browser_type import BrowserType

Initializer().ioOption()
xdriver = Initializer().chromeBrowserOption(BrowserType.CHROME, is_headless=False)

# ログインパスワードを取得 -------------------------------------------------------------------------------
# TODO:OSの環境変数に追加してそれを使うようにする
password_filepath = "C:\\Users\\nishigaki\\jupyter-lab\\password.txt"
password = OpenTextService().execute(
    x_text=XText(password_filepath), mode="r", encoding="UTF-8"
)


# ブラウザ起動 ---------------------------------------------------------------------------------------------------
webdriver = OpenBrowserService().execute(
    xbrowser=XBrowser(xdriver, XUrl("https://id.jobcan.jp/")),
    needs_multiple_tags=False,
)

# htmlを取得し値をセットして送信 -----------------------------------------------------------------------------------
# TODO:emailも外から渡すようにする
user_email = FindWebElementsService(SeleniumScraper(driver=webdriver)).by_id(
    "user_email"
)[0]

user_password = FindWebElementsService(SeleniumScraper(driver=webdriver)).by_id(
    "user_password"
)[0]

SetWebElementService().execute(
    XWebElementList(
        [
            XWebElement(
                user_email,
                "nishigaki@aivick.co.jp",
            ),
            XWebElement(
                user_password,
                password,
            ),
        ]
    )
)
FindWebElementsService(SeleniumScraper(driver=webdriver)).by_xpath(
    "//*[@id='new_user']/input[2]"
)[0].click()

sleep(1)

FindWebElementsService(SeleniumScraper(driver=webdriver)).by_class_name("jbc-app-link")[
    0
].click()
