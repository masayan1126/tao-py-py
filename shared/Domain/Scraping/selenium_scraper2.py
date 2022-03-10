from shared.Domain.Scraping.scraper import Scraper
from shared.Enums.ScrapingType import ScrapingType
from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumScraper2(Scraper):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_by_id(id_name: str):
        pass
