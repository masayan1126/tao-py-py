from shared.Domain.i_web_scraper import IWebScraper
from shared.Enums.ScrapingType import ScrapingType
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from bs4.element import Tag


class FindWebElementsService:
    def __init__(self, i_web_scraper: IWebScraper):
        self.web_scraper = i_web_scraper

    def by_tag_name(self, html_tag_name: str):
        if self.web_scraper.get_scraper_type() == ScrapingType.SELENIUM:
            return self.web_scraper.get_scraper().find_elements(
                By.TAG_NAME, html_tag_name
            )

        else:
            return self.web_scraper.get_scraper().select(html_tag_name)

    def by_class_name(self, html_class_name: str):
        if self.web_scraper.get_scraper_type() == ScrapingType.SELENIUM:
            return self.web_scraper.get_scraper().find_elements(
                By.CLASS_NAME, html_class_name
            )

        else:
            return self.web_scraper.get_scraper().select(html_class_name)

    def by_id(self, id_name: str) -> WebElement | Tag:
        if self.web_scraper.get_scraper_type() == ScrapingType.SELENIUM:
            return self.web_scraper.get_scraper().find_elements(By.ID, id_name)[0]

        else:
            return self.web_scraper.get_scraper().select(id_name)[0]

    def by_attr_name(self, attr_name: str):
        if self.web_scraper.get_scraper_type() == ScrapingType.SELENIUM:
            return self.web_scraper.get_scraper().find_elements(By.NAME, attr_name)

        else:
            return self.web_scraper.get_scraper().select(attr_name)

    def by_xpath(self, xpath: str):
        if self.web_scraper.get_scraper_type() == ScrapingType.SELENIUM:
            return self.web_scraper.get_scraper().find_elements(By.XPATH, xpath)[0]

        else:
            return self.web_scraper.get_scraper().select(xpath)

    def by_selector(self, selector: str):
        if self.web_scraper.get_scraper_type() == ScrapingType.SELENIUM:
            return self.web_scraper.get_scraper().find_elements(
                By.CSS_SELECTOR, selector
            )

        else:
            return self.web_scraper.get_scraper().select(selector)
