from abc import abstractmethod, ABCMeta
from typing import Optional
from bs4 import BeautifulSoup, ResultSet, Tag

# ブラウザ自動操作用インターフェース


class IHtmlAnalyzer(metaclass=ABCMeta):
    @abstractmethod
    def bind(self, beautiful_soup: BeautifulSoup) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id_name: str) -> Tag:
        pass

    @abstractmethod
    def find_by_selector(self, selector: str) -> Tag:
        pass

    @abstractmethod
    def search_by_selector(self, selector: str) -> Optional[ResultSet]:
        pass

    @abstractmethod
    def search_by_class(self, class_name: str) -> Optional[ResultSet]:
        pass
