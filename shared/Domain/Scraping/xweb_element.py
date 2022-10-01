from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement


@dataclass
class XWebElement:
    _web_element: WebElement
    _value: str = ""

    def web_element(self) -> WebElement:
        return self._web_element

    # 要素に対する値(ex.inputタグの要素に対する入力値等)
    def value(self) -> str:
        return self._value

    def set_value(self, value: str):
        self._value = value
        return self

    def click(self):
        self.web_element().click()
