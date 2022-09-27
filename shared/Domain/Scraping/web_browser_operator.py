from selenium.webdriver.common.by import By
from injector import inject
from shared.Domain.Converter.web_element_converter import WebElementConverter
from shared.Domain.Scraping.xbrowser import XBrowser
from selenium.common.exceptions import NoSuchElementException
from shared.Domain.Scraping.xweb_element import XWebElement
from shared.Domain.Scraping.xweb_element_list import XWebElementList


class WebBrowserOperator:
    @inject
    def boot(self, xbrowser: XBrowser, needs_multiple_tags: bool = False):
        webdriver = xbrowser.webdriver()
        self._webdriver = webdriver

        if needs_multiple_tags:
            # 新しいタブを作成する
            webdriver.execute_script("window.open()")

            # 新しいタブに切り替える
            webdriver.switch_to.window(webdriver.window_handles[-1])

        webdriver.get(xbrowser.url())
        webdriver.maximize_window()

        return xbrowser

    def find_by_id(self, id_name: str) -> XWebElement:
        def closure():
            return self._webdriver.find_element(By.ID, id_name)

        return self._handle(closure)

    def find_by_xpath(self, xpath: str) -> XWebElement:
        def closure():
            return self._webdriver.find_element(By.XPATH, xpath)

        return self._handle(closure)

    # TODO:
    def find_by_class_name(self, class_name: str) -> XWebElementList:
        return WebElementConverter().convert(
            self._webdriver.find_elements(By.CLASS_NAME, class_name)
        )

    def find_by_css_selector(self, css_selector: str) -> XWebElement:
        def closure():
            return self._webdriver.find_element(By.CSS_SELECTOR, css_selector)

        return self._handle(closure)

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

    def _handle(self, closure):
        try:
            web_element = closure()
            return WebElementConverter().convert([web_element]).first()

        except NoSuchElementException:
            # "対象のhtml要素が見つかりませんでした"
            raise NoSuchElementException

    def webdriver(self):
        return self._webdriver

    def switch_new_tab(self):
        return self.webdriver().switch_to.window(self.webdriver().window_handles[-1])
