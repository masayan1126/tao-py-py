from bs4 import BeautifulSoup
from shared.Domain.i_web_scraper import IWebScraper
from shared.Domain.xbeautiful_soup import XBeautifulSoup
from shared.Domain.xdriver import XDriver
from shared.Enums.ScrapingType import ScrapingType


class BeautifulSoupScraper(IWebScraper):
    def __init__(self, xbeautiful_soup: XBeautifulSoup):
        self.xbeautiful_soup = xbeautiful_soup

    def get_scraper_type(self):
        return ScrapingType.SOUP

    def get_scraper(self):
        return self.xbeautiful_soup.get_soup()
