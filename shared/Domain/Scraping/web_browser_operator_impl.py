from dataclasses import dataclass
from selenium.webdriver.common.by import By
from injector import inject
from shared.Domain.Converter.web_element_converter import WebElementConverter
from shared.Domain.Scraping.xweb_element import XWebElement
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from selenium.webdriver.remote.webdriver import WebDriver
from shared.Domain.Url.x_url import XUrl


@dataclass
class WebBrowserOperatorImpl:
    @inject
    def boot(
        self, webdriver: WebDriver, x_url: XUrl, needs_multiple_tags: bool = False
    ) -> None:
        self._webdriver = webdriver
        self._x_url = x_url
        if needs_multiple_tags:
            # 新しいタブを作成して切り替える
            self._webdriver.execute_script("window.open()")
            self._webdriver.switch_to.window(self._webdriver.window_handles[-1])

        self._webdriver.get(self._x_url.href())
        self._webdriver.maximize_window()

    def find_by_id(self, id_name: str) -> XWebElement:
        return (
            WebElementConverter()
            .convert([self._webdriver.find_element(By.ID, id_name)])
            .first()
        )

    def find_by_xpath(self, xpath: str) -> XWebElement:
        return (
            WebElementConverter()
            .convert([self._webdriver.find_element(By.XPATH, xpath)])
            .first()
        )

    def find_by_class_name(self, class_name: str) -> XWebElementList:
        return WebElementConverter().convert(
            self._webdriver.find_elements(By.CLASS_NAME, class_name)
        )

    def find_by_css_selector(self, css_selector: str) -> XWebElementList:
        return WebElementConverter().convert(
            self._webdriver.find_elements(By.CSS_SELECTOR, css_selector)
        )

    def search_by_css_selector(self, css_selector: str) -> XWebElementList:
        return WebElementConverter().convert(
            self._webdriver.find_elements(By.CSS_SELECTOR, css_selector)
        )

    def send_value(self, web_element_list: XWebElementList) -> None:
        list(
            map(
                lambda xweb_element: xweb_element.web_element().send_keys(
                    xweb_element.value()
                ),
                web_element_list.all(),
            )
        )

    def web_driver(self) -> WebDriver:
        return self._webdriver

    def switch_new_tab(self, to: str = None):
        self._webdriver.switch_to.window(self._webdriver.window_handles[-1])

        if to is not None:
            self.web_driver().get(to)
