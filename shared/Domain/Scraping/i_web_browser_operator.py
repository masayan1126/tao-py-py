from abc import *
from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from shared.Domain.Scraping.xbrowser import XBrowser
from shared.Domain.Scraping.xweb_element import XWebElement
from shared.Domain.Scraping.xweb_element_list import XWebElementList

# ブラウザ自動操作用インターフェース
class IWebBrowserOperator(metaclass=ABCMeta):
    @abstractmethod
    def boot(self, xbrowser: XBrowser, needs_multiple_tags: bool = False) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id_name: str) -> XWebElement:
        pass

    @abstractmethod
    def find_by_xpath(self, xpath: str) -> XWebElement:
        pass

    @abstractmethod
    def find_by_class_name(
        self, webdriver: WebDriver, class_name: str
    ) -> List[XWebElement]:
        pass

    @abstractmethod
    def send_value(self, web_element_list: XWebElementList) -> None:
        pass
