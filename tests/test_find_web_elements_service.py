from bs4 import BeautifulSoup
import bs4
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.remote.webelement import WebElement
from shared.Application.find_web_elements_service import FindWebElementsService
from shared.Application.open_browser_service import OpenBrowserService
from shared.Domain.Converter.web_element_converter import WebElementConverter
from shared.Domain.Scraping.beautiful_soup_scraper import BeautifulSoupScraper
from shared.Domain.Scraping.selenium_scraper import SeleniumScraper
from shared.Domain.xbeautiful_soup import XBeautifulSoup
from shared.Domain.xbrowser import XBrowser
from shared.Domain.xdriver import XDriver
from shared.Domain.xurl import XUrl
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import requests
from shared.Domain.xweb_element import XWebElement

from shared.Domain.xweb_element_list import XWebElementList


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
    chrome_options.add_argument("--headless")
    chrome_service = fs.Service(executable_path=ChromeDriverManager().install())
    xdriver = XDriver(chrome_service, chrome_options, "Chrome")
    driver = OpenBrowserService().execute(
        xbrowser=XBrowser(xdriver, XUrl("https://maasaablog.com/")),
        needs_multiple_tags=False,
    )

    return driver


def test_タグ名で全要素を取得できること(setuped_driver):
    web_element_list = FindWebElementsService(
        SeleniumScraper(driver=setuped_driver)
    ).by_tag_name("h1")

    x_web_element_list_1 = WebElementConverter.convert(web_element_list)
    x_web_element_list_2 = XWebElementList(web_elements=[])

    x_web_element_list_2.add(
        XWebElement(
            web_element_list[0],
            "",
        )
    )

    assert x_web_element_list_1 == x_web_element_list_2


def test_タグ名で全要素を取得できること_bs():

    res = requests.get("https://maasaablog.com/")
    xbeautiful_soup = XBeautifulSoup(BeautifulSoup(res.text, "html.parser"))

    elems = FindWebElementsService(
        BeautifulSoupScraper(xbeautiful_soup=xbeautiful_soup)
    ).by_tag_name("h1")

    assert elems[0].text == "masayanblog"


def test_クラス名で全要素を取得できること(setuped_driver):
    elems = FindWebElementsService(
        SeleniumScraper(driver=setuped_driver)
    ).by_class_name("logo-text")

    assert elems[0].text == "masayanblog"
    # assert type(elems) == "masayanblog"


def test_ID名で要素を取得できること(setuped_driver):
    elems = FindWebElementsService(SeleniumScraper(driver=setuped_driver)).by_id(
        "header-in"
    )

    assert elems[0].text == "masayanblog"


def test_name属性で全要素を取得できること(setuped_driver):
    # 例) <input name="s" placeholder="サイト内を検索" />
    elems = FindWebElementsService(SeleniumScraper(driver=setuped_driver)).by_attr_name(
        "s"
    )

    elem: WebElement = elems[0]
    assert elem.get_property("placeholder") == "サイト内を検索"


def test_xpathで全要素を取得できること(setuped_driver):
    elems = FindWebElementsService(SeleniumScraper(driver=setuped_driver)).by_xpath(
        "//*[@id='header-in']/h1"
    )

    assert elems[0].text == "masayanblog"


def test_cssセレクタで全要素を取得できること(setuped_driver):
    elems = FindWebElementsService(SeleniumScraper(driver=setuped_driver)).by_selector(
        ".logo-text"
    )

    assert elems[0].text == "masayanblog"
