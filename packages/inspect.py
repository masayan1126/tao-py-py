from bs4 import BeautifulSoup
import bs4
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from shared.Application.find_web_elements_service import FindWebElementsService
from shared.Application.open_browser_service import OpenBrowserService
from shared.Domain.Converter.web_element_converter import WebElementConverter
from shared.Domain.Scraping.beautiful_soup_scraper import BeautifulSoupScraper
from selenium.webdriver.remote.webelement import WebElement
from shared.Domain.xbeautiful_soup import XBeautifulSoup
from shared.Domain.Scraping.selenium_scraper import SeleniumScraper
from shared.Domain.xbrowser import XBrowser
from shared.Domain.xdriver import XDriver
from shared.Domain.xurl import XUrl
from webdriver_manager.chrome import ChromeDriverManager
from shared.Domain.xweb_element import XWebElement

from shared.Domain.xweb_element_list import XWebElementList


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_experimental_option("detach", True)  # 処理完了後もブラウザが起動している状態を保持する
chrome_service = fs.Service(executable_path=ChromeDriverManager().install())
xdriver = XDriver(chrome_service, chrome_options, "Chrome")
driver = OpenBrowserService().execute(
    xbrowser=XBrowser(xdriver, XUrl("https://maasaablog.com/")),
    needs_multiple_tags=False,
)

web_element_list = FindWebElementsService(SeleniumScraper(driver=driver)).by_tag_name(
    "h1"
)

x_web_element_list_1 = WebElementConverter.convert(web_element_list)
x_web_element_list_2 = XWebElementList(web_elements=[])

x_web_element_list_2.add(
    XWebElement(
        web_element_list[0],
        "",
    )
)


print(x_web_element_list_1, x_web_element_list_2)
print(x_web_element_list_2 == x_web_element_list_1)
