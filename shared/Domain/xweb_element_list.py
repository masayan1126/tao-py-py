from typing import List
from shared.Domain.xweb_element import XWebElement
from functools import total_ordering


@total_ordering
class XWebElementList:
    def __init__(self, web_elements: List[XWebElement] = []):
        self.web_element_list = []
        list(map(lambda web_element: self.add(web_element), web_elements))

    def __eq__(self, other):
        if not isinstance(other, XWebElementList):
            return NotImplemented
        return (self.web_element_list) == (other.web_element_list)

    def __lt__(self, other):
        if not isinstance(other, XWebElementList):
            return NotImplemented
        return (self.web_element_list) < (other.web_element_list)

    def add(self, web_element):
        self.web_element_list.append(web_element)

    def all(self) -> List[XWebElement]:
        return self.web_element_list

    def count(self):
        return len(self.all())

    def is_empty(self):
        return self.count() == 0

    def first(self) -> XWebElement | IndexError:
        if self.is_empty():
            raise IndexError
        else:
            return self.all()[0]
