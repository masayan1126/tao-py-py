import io, sys
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from webdriver_manager.chrome import ChromeDriverManager
from shared.Domain.Scraping.xdriver import XDriver
from shared.Enums.browser_type import BrowserType


class Initializer:
    def ioOption(self) -> None:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
