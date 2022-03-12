from abc import *
from bs4 import BeautifulSoup, ResultSet

# ブラウザ自動操作用インターフェース
class IHtmlAnalyzer(metaclass=ABCMeta):
    @abstractmethod
    def bind(self, beautiful_soup: BeautifulSoup) -> None:
        pass

    @abstractmethod
    def find_by_id(self, css_selector: str) -> ResultSet:
        pass

    # @abstractmethod
    # def find_by_class_name(
    #     self, webdriver: WebDriver, class_name: str
    # ) -> List[XWebElement]:
    #     pass

    # @abstractmethod
    # def send_value(self, web_element_list: XWebElementList) -> None:
    #     pass
