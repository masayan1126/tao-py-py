from bs4 import BeautifulSoup
import pytest
import requests
from shared.Application.open_browser_service import OpenBrowserService
from shared.Domain.beautiful_soup_scraper import BeautifulSoupScraper
from shared.Domain.selenium_scraper import SeleniumScraper
from shared.Domain.xbeautiful_soup import XBeautifulSoup
from shared.Application.find_web_element_service import FindWebElementService
from shared.Domain.xbrowser import XBrowser
from shared.Domain.xdriver import XDriver
from shared.Domain.xurl import XUrl
from shared.Enums.ScrapingType import ScrapingType
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setuped_xbeautiful_soup():
    base_path = "https://maasaablog.com/"
    res = requests.get(base_path)
    return XBeautifulSoup(BeautifulSoup(res.text, "html.parser"))


@pytest.fixture
def setuped_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_experimental_option("detach", True)  # 処理完了後もブラウザが起動している状態を保持する
    chrome_service = fs.Service(executable_path=ChromeDriverManager().install())
    xdriver = XDriver(chrome_service, chrome_options, "Chrome")
    driver = OpenBrowserService().execute(
        xbrowser=XBrowser(xdriver, XUrl("https://maasaablog.com/")),
        needs_multiple_tags=False,
    )

    return driver


def test_対象のページからhtml要素を取得できること_soup(setuped_xbeautiful_soup: XBeautifulSoup):
    title_tag_list = FindWebElementService(
        BeautifulSoupScraper(xbeautiful_soup=setuped_xbeautiful_soup)
    ).find_element_by_tag_name("title")
    assert title_tag_list[0].text == "masayanblog | 現役のweb系エンジニアが役立つ情報をまったりご紹介"


def test_対象のページからhtml要素を取得できること_selenium(setuped_driver):
    header_tag_list = FindWebElementService(
        SeleniumScraper(driver=setuped_driver)
    ).find_element_by_tag_name("header")

    assert header_tag_list[0].text == "masayanblog"
