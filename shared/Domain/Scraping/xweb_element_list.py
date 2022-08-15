from __future__ import annotations
from dataclasses import dataclass
from typing import Callable
from shared.Domain.List.array_impl import ArrayImpl
from shared.Domain.Scraping.xweb_element import XWebElement


@dataclass
class XWebElementList(ArrayImpl):
    def __init__(self, xweb_element_list: list[XWebElement]):
        super().__init__(xweb_element_list)

    def all(self) -> list[XWebElement]:
        return super().all()

    def add(self, xweb_element: XWebElement) -> XWebElementList:
        super().add(xweb_element)
        return self

    def map(self, callable: Callable) -> XWebElementList:

        super().map(callable)
        return self

    def first(self) -> XWebElement:
        try:
            return super().first()
        except IndexError:

            raise IndexError
