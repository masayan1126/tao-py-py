from typing import List
from shared.Domain.xweb_element import XWebElement

class WebElementList:
    def __init__(self, web_elements: List[XWebElement]):
        list(map(lambda web_element: self.add(web_element), web_elements))

    def add(self, web_element):
        self.web_elements.append(web_element)

    def get_web_elements(self):
        return self.web_elements

    def count(self):
        return len(self.web_elements)
