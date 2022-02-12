from shared.Domain.i_web_scraper import IWebScraper
from bs4 import BeautifulSoup

from shared.Enums.ScrapingType import ScrapingType


class XBeautifulSoup:
    def __init__(self, soup: BeautifulSoup):
        self.soup = soup

    def get_soup(self):
        return self.soup
