from bs4 import BeautifulSoup
import bs4
from selenium import webdriver
import requests
import file_downloader.main
from shared.Domain.xurl import XUrl

from selenium.webdriver.chrome import service as fs
from selenium.webdriver.remote.webelement import WebElement
from shared.Application.find_web_elements_service import FindWebElementsService
from shared.Application.open_browser_service import OpenBrowserService
from shared.Domain.Converter.web_element_converter import WebElementConverter
from shared.Domain.Scraping.beautiful_soup_scraper import BeautifulSoupScraper
from shared.Domain.Scraping.selenium_scraper import SeleniumScraper
from shared.Domain.xbeautiful_soup import XBeautifulSoup
from shared.Domain.xbrowser import XBrowser

from shared.Enums.ScrapingType import ScrapingType
from shared.Enums.browser_type import BrowserType

xurl = XUrl("https://maasaablog.com/")
res = requests.get(xurl.get_href())
xbeautiful_soup = XBeautifulSoup(BeautifulSoup(res.text, "html.parser"))

web_element_list = FindWebElementsService(
    BeautifulSoupScraper(xbeautiful_soup=xbeautiful_soup)
).by_tag_name("h2")

print(WebElementConverter().convert(web_element_list).all()[0])

# xdriver = InitChromeBrowserOption().execute(BrowserType.CHROME)
# from bs4 import BeautifulSoup
# import bs4
# from selenium import webdriver
# import requests

# from selenium.webdriver.chrome import service as fs
# from selenium.webdriver.remote.webelement import WebElement
# from shared.Application.find_web_elements_service import FindWebElementsService
# from shared.Application.open_browser_service import OpenBrowserService
# from shared.Domain.Converter.web_element_converter import WebElementConverter
# from shared.Domain.Scraping.beautiful_soup_scraper import BeautifulSoupScraper
# from shared.Domain.Scraping.selenium_scraper import SeleniumScraper
# from shared.Domain.xbeautiful_soup import XBeautifulSoup
# from shared.Domain.xbrowser import XBrowser

# from shared.Domain.xurl import XUrl
# from shared.Enums.ScrapingType import ScrapingType
# from shared.Enums.browser_type import BrowserType

# from __future__ import unicode_literals
# import youtube_dl

# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(["https://www.youtube.com/watch?v=CFLOiR2EbKM"])


# xurl = XUrl("https://maasaablog.com/")
# res = requests.get(xurl.get_href())
# xbeautiful_soup = XBeautifulSoup(BeautifulSoup(res.text, "html.parser"))

# web_element_list = FindWebElementsService(
#     BeautifulSoupScraper(xbeautiful_soup=xbeautiful_soup)
# ).by_tag_name("h2")

# print(WebElementConverter().convert(web_element_list).all()[0])

# xdriver = InitChromeBrowserOptionService().execute(BrowserType.CHROME)

# driver = OpenBrowserService().execute(
#     xbrowser=XBrowser(xdriver, XUrl("https://maasaablog.com/")),
#     needs_multiple_tags=False,
# )

# web_element_list = FindWebElementsService(SeleniumScraper(driver=driver)).by_tag_name(
#     "h3"
# )

# x_web_element_list_1 = WebElementConverter.convert(web_element_list)
# print(x_web_element_list_1.count())
