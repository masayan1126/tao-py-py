from abc import ABCMeta, abstractmethod
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
    def find_by_class_name(self, class_name: str) -> XWebElementList:
        pass

    @abstractmethod
    def find_by_css_selector(self, css_selector: str) -> XWebElement:
        pass

    @abstractmethod
    def search_by_css_selector(self, css_selector: str) -> XWebElementList:
        pass

    @abstractmethod
    def send_value(self, web_element_list: XWebElementList) -> None:
        pass

    @abstractmethod
    def webdriver(self) -> WebDriver:
        pass

    @abstractmethod
    def switch_new_tab(self) -> None:
        pass
