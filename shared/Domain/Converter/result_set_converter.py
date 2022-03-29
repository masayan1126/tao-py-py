from typing import List
from shared.Domain.Scraping.xweb_element import XWebElement
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from selenium.webdriver.remote.webelement import WebElement
from bs4 import BeautifulSoup, ResultSet


class ResultSetConverter:
    @staticmethod
    def convert(result_set: ResultSet):

        array = []

        for result in result_set:
            array.append(result)

        return array
