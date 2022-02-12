from shared.Domain.i_xweb_element import IXWebElement
from selenium.webdriver.remote.webelement import WebElement


class XWebElement(IXWebElement):
    def __init__(self, element: WebElement, value):
        self.element = element
        self.value = value

    def get_element(self):
        return self.element

    def get_value(self):
        return self.value
