from selenium.webdriver.remote.webdriver import WebDriver


class XDriver:
    def __init__(self, webdriver: WebDriver) -> None:
        self.webdriver = webdriver

    def driver(self) -> WebDriver:
        return self.webdriver
