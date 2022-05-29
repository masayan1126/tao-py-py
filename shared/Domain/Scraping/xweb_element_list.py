from typing import Callable, List
from shared.Domain.Scraping.xweb_element import XWebElement
from functools import total_ordering


@total_ordering
class XWebElementList:
    def __init__(self, xweb_elements: list[XWebElement]):
        self._xweb_element_list: list[XWebElement] = []

        if len(xweb_elements) != 0:
            for xweb_element in xweb_elements:
                self.add(xweb_element)

    def __eq__(self, other):
        if not isinstance(other, XWebElementList):
            return NotImplemented
        return (self._xweb_element_list) == (other._xweb_element_list)

    def __lt__(self, other):
        if not isinstance(other, XWebElementList):
            return NotImplemented
        return (self._xweb_element_list) < (other._xweb_element_list)

    def xweb_element_list(self):
        return self

    def add(self, xweb_element):
        self._xweb_element_list.append(xweb_element)
        return self

    def all(self) -> list[XWebElement]:
        return self._xweb_element_list

    def count(self) -> int:
        return len(self._xweb_element_list)

    def map(self, callable: Callable):
        list(map(lambda xweb_element: callable(xweb_element), self.all()))
        return self

    def is_empty(self) -> bool:
        return self.count() == 0

    def first(self) -> XWebElement:
        try:
            return self.all()[0]
        except IndexError:

            raise IndexError
