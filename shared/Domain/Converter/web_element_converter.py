from typing import List
from shared.Domain.xweb_element import XWebElement
from shared.Domain.xweb_element_list import XWebElementList
from selenium.webdriver.remote.webelement import WebElement


class WebElementConverter:
    @staticmethod
    def convert(iterable: List[WebElement]):

        xweb_element_list = XWebElementList([])

        for item in iterable:
            xweb_element_list.add(XWebElement(item, ""))

        return xweb_element_list
