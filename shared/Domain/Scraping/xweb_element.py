from selenium.webdriver.remote.webelement import WebElement
from functools import total_ordering
from shared.base_class import BaseClass


@total_ordering
class XWebElement(BaseClass):
    def __init__(self, web_element: WebElement, value: str):
        self._web_element = web_element
        self._value = value

    def __str__(self):
        return f"html要素: {self._web_element}\n送信する値: {self._value}"

    def __eq__(self, other):
        if not isinstance(other, XWebElement):
            return NotImplemented
        return (self._web_element, self._value) == (other._web_element, other._value)

    def __lt__(self, other):
        if not isinstance(other, XWebElement):
            return NotImplemented
        return (self._web_element, self._value) < (other._web_element, other._value)

    def web_element(self) -> WebElement:
        return self._web_element

    def value(self) -> str:
        return self._value

    def set_value(self, value):
        self._value = value
        return self
