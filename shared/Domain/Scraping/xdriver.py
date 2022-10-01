from dataclasses import dataclass
from selenium.webdriver.remote.webdriver import WebDriver


@dataclass
class XDriver:
    webdriver: WebDriver

    def driver(self) -> WebDriver:
        return self.webdriver
