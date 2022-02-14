from typing import List
from shared.Domain.xweb_element import XWebElement


class XWebElementList:
    def __init__(self, web_elements: List[XWebElement]):
        self.web_element_list = []
        list(map(lambda web_element: self.add(web_element), web_elements))

    def add(self, web_element):
        self.web_element_list.append(web_element)

    def get_web_element_list(self) -> List[XWebElement]:
        return self.web_element_list

    def count(self):
        return len(self.web_elements)
