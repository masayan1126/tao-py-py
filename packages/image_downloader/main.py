import io, sys
import requests

import io
from shared.Domain.xurl import XUrl
from shared.Application.check_is_valid_url_service import CheckIsValidUrlService
from shared.Application.download_image_service import DownloadImageService
from shared.Domain.ximage import XImage
from shared.Application.find_web_element_service import FindWebElementService
from shared.Domain.xbeautiful_soup import XBeautifulSoup
from bs4 import BeautifulSoup
from shared.Domain.xcsv import XCsv
from shared.Domain.Scraping.selenium_scraper import SeleniumScraper
from shared.Enums.ScrapingType import ScrapingType

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# 対象のurlからBeautifulSoupのオブジェクト(html)を生成
base_path = "https://maasaablog.com/"
target_dir = ""
image_dir_path = base_path + "assets/img/top"
download_path_from = base_path + target_dir
res = requests.get(download_path_from)

xbeautiful_soup = XBeautifulSoup(BeautifulSoup(res.text, "html.parser"))
image_tag_list = FindWebElementService(
    SeleniumScraper(ScrapingType.SOUP)
).find_by_html_tag_name("img")

image_list_df = XCsv().read(
    filepath="C:\\Users\\nishigaki\\Desktop\\image_list.csv",
    encoding="shift-jis",
    header=0,
)
column = "from"
image_name_list = image_list_df[column].to_list()
download_path_to = "C:\\Users\\nishigaki\\Desktop\\"

# 画像URLからダウンロード
for image_url in image_name_list:
    x_url = XUrl(url=image_url)
    if not CheckIsValidUrlService().execute(x_url):
        exit()

    x_image = XImage(src=image_url, alt="")
    DownloadImageService().execute(x_image=x_image, download_path_to=download_path_to)
