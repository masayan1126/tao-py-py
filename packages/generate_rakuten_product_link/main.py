import io, sys
import requests

import io
from shared.Application.open_text_service import OpenTextService
from shared.Domain.xtext import XText
from shared.Application.find_web_element_service import FindWebElementService
from shared.Domain.xbeautiful_soup import XBeautifulSoup
from bs4 import BeautifulSoup

from shared.Domain.Scraping.beautiful_soup_scraper import BeautifulSoupScraper
from shared.Enums.ScrapingType import ScrapingType

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")


url_filepath = "C:\\Users\\nishigaki\\jupyter-lab\\packages\\generate_rakuten_product_link\\url.txt"
url = OpenTextService().execute(x_text=XText(url_filepath), mode="r", encoding="UTF-8")

res = requests.get(url)
xbeautiful_soup = XBeautifulSoup(BeautifulSoup(res.text, "html.parser"))
atag_resultset = FindWebElementService(
    BeautifulSoupScraper(xbeautiful_soup)
).find_element_by_selector(".review-title")

# 途中で実装中止
