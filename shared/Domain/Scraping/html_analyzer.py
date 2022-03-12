import sys
from shared.Domain.Scraping.i_html_analyzer import IHtmlAnalyzer
from bs4 import BeautifulSoup, ResultSet

from shared.x_logger import XLogger


class HtmlAnalyzer(IHtmlAnalyzer):
    def bind(self, beautiful_soup: BeautifulSoup):
        self.beautiful_soup = beautiful_soup

    def find_by_id(self, css_selector: str) -> ResultSet:
        try:
            return self.beautiful_soup.select(css_selector)[0]
        except IndexError:
            XLogger.exceptionToSlack("対象のhtml要素が見つかりませんでした")
            XLogger.exception("対象のhtml要素が見つかりませんでした")
            sys.exit()

    # def send_value(self, web_element_list: XWebElementList) -> None:
    #     pass
