from time import sleep

from attr import attributes

from shared.Domain.xbeautiful_soup import XBeautifulSoup


class FindWebElementService:
    def __init__(self, xbeautiful_soup: XBeautifulSoup):
        self.xbeautiful_soup = xbeautiful_soup

    def find_element_by_tag_name(self, html_tag_name: str):
        return self.xbeautiful_soup.get_soup().find_all(html_tag_name)

    def find_element_by_selector(self, selector: str):
        return self.xbeautiful_soup.get_soup().select(selector)
