from bs4 import BeautifulSoup
from shared.Domain.i_web_scraper import IWebScraper
from shared.Domain.xbeautiful_soup import XBeautifulSoup
from shared.Domain.xbrowser import XBrowser
from shared.Domain.xdriver import XDriver
from shared.Enums.ScrapingType import ScrapingType


class SeleniumScraper(IWebScraper):
    def __init__(self, driver):
        self.driver = driver

    def get_scraper_type(self):
        return ScrapingType.SELENIUM

    def get_scraper(self):
        return self.driver
