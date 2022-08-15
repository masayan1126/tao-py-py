from shared.Domain.Scraping.xweb_element import XWebElement
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from selenium.webdriver.remote.webelement import WebElement


class WebElementConverter:
    @staticmethod
    # webelementのリストを受け取り、xwebelementのリストを返します
    def convert(web_element_list: list[WebElement]) -> XWebElementList:

        xweb_element_list = XWebElementList([])

        for web_element in web_element_list:
            xweb_element_list.add(XWebElement(web_element, ""))

        return xweb_element_list
