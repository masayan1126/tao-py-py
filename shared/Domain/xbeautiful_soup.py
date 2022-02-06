

from bs4 import BeautifulSoup


class XBeautifulSoup:
    def __init__(self, soup: BeautifulSoup):
        self.soup = soup
        
    def get_soup(self):
        return self.soup