from selenium import webdriver
from shared.Domain.i_web_scraper import IWebScraper
from shared.Enums.ScrapingType import ScrapingType
# from selenium selenium.common.exceptions.SessionNotCreatedException


class XDriver:
    def __init__(self, service, options, type):
        self.service = service
        self.options = options
        self.type = type

    def get_driver(self):
        if self.type == "Chrome":
            try:
                return webdriver.Chrome(service=self.service, options=self.options)
            except:
                
                "webdriverのバージョンがChromeブラウザーのバージョンと一致していないため起動に失敗しました。"
