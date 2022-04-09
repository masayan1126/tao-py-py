from typing import Optional
from shared.Domain.Scraping.i_html_analyzer import IHtmlAnalyzer
from bs4 import BeautifulSoup, ResultSet, Tag


class HtmlAnalyzer(IHtmlAnalyzer):
    def bind(self, beautiful_soup: BeautifulSoup) -> None:
        self.beautiful_soup = beautiful_soup

    def find_by_id(self, id_name: str) -> Tag:
        try:
            # 要素が見つからない場合は例外を出したいので、find_allで配列で取得し、キーを指定する
            return self.beautiful_soup.find_all(id=id_name)[0]
        except IndexError:
            # "対象のhtml要素が見つかりませんでした"
            raise IndexError

    def find_by_selector(self, selector: str) -> Tag:
        try:
            return self.beautiful_soup.select(selector)[0]
        except IndexError:
            # "対象のhtml要素が見つかりませんでした"
            raise IndexError

    def search_by_class(self, class_name: str) -> Optional[ResultSet]:
        return self.beautiful_soup.find_all(class_=class_name)
