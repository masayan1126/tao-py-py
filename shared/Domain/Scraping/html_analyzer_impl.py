from typing import Optional
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer
from bs4 import BeautifulSoup, ResultSet, Tag


class HtmlAnalyzerImpl(HtmlAnalyzer):
    def bind(self, beautiful_soup: BeautifulSoup) -> None:
        self.beautiful_soup = beautiful_soup

    def find_by_id(self, id_name: str) -> Tag:
        try:
            # 要素が見つからない場合は例外を出したいので、find_allで配列で取得し、キーを指定する
            return self.beautiful_soup.find_all(id=id_name)[0]
        except IndexError:
            raise IndexError

    # memo: xpathはそこそこ頑張らないと実装できない

    def find_by_selector(self, selector: str) -> Tag:
        try:
            return self.beautiful_soup.select(selector)[0]
        except IndexError:
            raise IndexError

    def search_by_selector(self, selector: str) -> Optional[ResultSet]:
        return self.beautiful_soup.select(selector)

    def search_by_class(self, class_name: str) -> Optional[ResultSet]:
        return self.beautiful_soup.find_all(class_=class_name)
