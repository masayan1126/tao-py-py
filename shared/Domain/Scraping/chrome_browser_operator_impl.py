from dataclasses import dataclass
from selenium.webdriver.common.by import By
from shared.Domain.Scraping.web_element_converter import WebElementConverter
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.Scraping.xweb_element import XWebElement
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.Domain.Url.x_url import XUrl
from selenium.webdriver.chrome import service as fs
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import Chrome


@dataclass
class ChromeBrowserOperatorImpl(WebBrowserOperator):
    def __init__(self, url: XUrl, is_headless, needs_multiple_tabs: bool = False):
        service = fs.Service(executable_path=ChromeDriverManager().install())

        options = webdriver.ChromeOptions()
        # Chrome は自動テストソフトウェアによって制御されています。の表示とログ出力を非表示に
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation", "enable-logging"]
        )

        # 処理完了後もブラウザが起動している状態を保持する
        options.add_experimental_option("detach", True)

        if is_headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")

        self.__webdriver = Chrome(service=service, options=options)
        self._x_url = url

        if needs_multiple_tabs:
            # 新しいタブを作成して切り替える
            self.__webdriver.execute_script("window.open()")
            self.__webdriver.switch_to.window(self.__webdriver.window_handles[-1])

        self.__webdriver.get(self._x_url.url())
        self.__webdriver.maximize_window()

    def _webdriver(self):
        return self.__webdriver

    def find_by_id(self, id_name: str) -> XWebElement:
        return (
            WebElementConverter()
            .convert([self._webdriver().find_element(By.ID, id_name)])
            .first()
        )

    def find_by_xpath(self, xpath: str) -> XWebElement:
        return (
            WebElementConverter()
            .convert([self._webdriver().find_element(By.XPATH, xpath)])
            .first()
        )

    def find_by_class_name(self, class_name: str) -> XWebElementList:
        return WebElementConverter().convert(
            self._webdriver().find_elements(By.CLASS_NAME, class_name)
        )

    def find_by_css_selector(self, css_selector: str) -> XWebElementList:
        return WebElementConverter().convert(
            self._webdriver().find_elements(By.CSS_SELECTOR, css_selector)
        )

    def search_by_css_selector(self, css_selector: str) -> XWebElementList:
        return WebElementConverter().convert(
            self._webdriver().find_elements(By.CSS_SELECTOR, css_selector)
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

    def switch_new_tab(self, to: str = None):
        self._webdriver().switch_to.window(self._webdriver().window_handles[-1])

        if to is not None:
            self._webdriver().get(to)
