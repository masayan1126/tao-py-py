from shared.Domain.i_web_scraper import IWebScraper
from shared.Domain.xbeautiful_soup import XBeautifulSoup
from shared.Domain.xdriver import XDriver
from shared.Enums.ScrapingType import ScrapingType
from selenium.webdriver.common.by import By


class FindWebElementService:
    def __init__(self, i_web_scraper: IWebScraper):
        self.web_scraper = i_web_scraper

    def find_element_by_tag_name(self, html_tag_name: str):
        if self.web_scraper.get_scraper_type() == ScrapingType.SELENIUM:
            return self.web_scraper.get_scraper().find_elements_by_tag_name(
                html_tag_name
            )

        else:
            return self.web_scraper.get_scraper().find_all(html_tag_name)

    def find_element_by_selector(self, selector: str):
        return self.web_scraper.get_scraper().select(selector)

    def find_element_by_id(self, id_name: str):
        return self.web_scraper.get_scraper().find_element(By.ID, id_name)

    def find_element_by_xpath(self, xpath: str):
        return self.web_scraper.get_scraper().find_element(By.XPATH, xpath)
