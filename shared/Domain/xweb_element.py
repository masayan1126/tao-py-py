from shared.Domain.i_xweb_element import IXWebElement
from selenium.webdriver.remote.webelement import WebElement
from functools import total_ordering


@total_ordering
class XWebElement(IXWebElement):
    def __init__(self, element: WebElement, value):
        self.element = element
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, XWebElement):
            return NotImplemented
        return (self.element, self.value) == (other.element, self.value)

    def __lt__(self, other):
        if not isinstance(other, XWebElement):
            return NotImplemented
        return (self.element, self.value) < (other.element, self.value)

    def get_element(self):
        return self.element

    def get_value(self):
        return self.value
