from __future__ import annotations
from dataclasses import dataclass
from typing import Callable
from shared.Core.abstract_array import AbstractArray
from shared.Domain.Scraping.xweb_element import XWebElement


@dataclass
class XWebElementList(AbstractArray):
    def __init__(self, xweb_element_list: list[XWebElement] = []):
        super().__init__(xweb_element_list)

    def all(self) -> list[XWebElement]:
        return super().all()

    def add(self, xweb_element: XWebElement) -> XWebElementList:
        super().add(xweb_element)
        return self

    def map(self, callable: Callable) -> XWebElementList:
        return XWebElementList(list(map(lambda item: callable(item), self.all())))

    def first(self) -> XWebElement:
        return super().first()
