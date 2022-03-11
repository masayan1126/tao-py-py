from selenium.webdriver.remote.webelement import WebElement
from functools import total_ordering
from shared.base_class import BaseClass

# @total_ordering
class XWebElement(BaseClass):
    def __init__(self, element: WebElement, value):
        self.element = element
        self.value = value

    def __str__(self):
        return f"html要素: {self.element}\n送信する値: {self.value}"

    def __eq__(self, other):
        if not isinstance(other, XWebElement):
            return NotImplemented
        return (self.element, self.value) == (other.element, other.value)

    def __lt__(self, other):
        if not isinstance(other, XWebElement):
            return NotImplemented
        return (self.element, self.value) < (other.element, other.value)

    def get_element(self):
        return self.element

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        return self
