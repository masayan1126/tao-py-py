from abc import *
import sys
from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from injector import inject
from shared.Domain.Converter.web_element_converter import WebElementConverter
from shared.Domain.Scraping.xbrowser import XBrowser
from selenium.common.exceptions import NoSuchElementException
from shared.Domain.Scraping.xweb_element import XWebElement
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.x_logger import XLogger


class WebBrowserOperator:
    @inject
    def boot(self, xbrowser: XBrowser, needs_multiple_tags: bool = False):
        webdriver = xbrowser.webdriver()
        self.webdriver = webdriver

        if needs_multiple_tags:
            # 新しいタブを作成する
            webdriver.execute_script("window.open()")

            # 新しいタブに切り替える
            webdriver.switch_to.window(webdriver.window_handles[-1])

        webdriver.get(xbrowser.url())
        webdriver.maximize_window()

    def find_by_id(self, id_name: str) -> XWebElement:
        def closure():
            web_element = self.webdriver.find_element(By.ID, id_name)
            return WebElementConverter().convert([web_element]).first()

        return self._handle(closure)

    def find_by_xpath(self, xpath: str) -> XWebElement:
        def closure():
            web_element = self.webdriver.find_element(By.XPATH, xpath)
            return WebElementConverter().convert([web_element]).first()

        return self._handle(closure)

    # TODO:
    def find_by_class_name(
        self, webdriver: WebDriver, class_name: str
    ) -> List[XWebElement]:
        return webdriver.find_elements(By.CLASS_NAME, class_name)

    def send_value(self, web_element_list: XWebElementList) -> None:
        list(
            map(
                lambda xweb_element: xweb_element.web_element().send_keys(
                    xweb_element.value()
                ),
                web_element_list.all(),
            )
        )

    def _handle(self, closure):
        try:
            return closure()

        except NoSuchElementException:
            XLogger.exceptionToSlack("対象のhtml要素が見つかりませんでした")
            XLogger.exception("対象のhtml要素が見つかりませんでした")
            sys.exit()
