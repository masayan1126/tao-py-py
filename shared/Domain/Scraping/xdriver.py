from shared.x_logger import XLogger
from selenium import webdriver


class XDriver:
    def __init__(self, webdriver):
        self.webdriver = webdriver

    def driver(self):
        return self.webdriver
