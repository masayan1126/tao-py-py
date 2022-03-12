import io, sys
from pprint import pprint
from typing import List
import pandas as pd
import requests
from selenium.webdriver.remote.webelement import WebElement
import io
from shared.Domain.Converter.data_frame_converter import DataFrameConverter
from shared.Domain.xurl import XUrl
from shared.Application.check_is_valid_url_service import CheckIsValidUrlService
from shared.Application.download_image_service import DownloadImageService
from shared.Domain.ximage import XImage
from shared.Domain.Scraping.xbeautiful_soup import XBeautifulSoup
from bs4 import BeautifulSoup
from shared.Domain.xcsv import XCsv
from shared.Domain.Scraping.html_analyzer import BeautifulSoupScraper
from shared.Enums.ScrapingType import ScrapingType

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# 1.対象のurlの一覧をcsvから読み込む
# 2.対象のurlから特定の要素のリストを取得する
# 3.2.のリストをcsvに出力する
# 4.3のcsvを読み取り、画像をダウンロードする

# get_webelement_the_url

url_list_df = XCsv().read(
    filepath="C:\\Users\\nishigaki\\Desktop\\url_list.csv",
    encoding="utf_8_sig",
    header=0,
)
column = "url"
url_list = url_list_df[column].to_list()

image_tag_list = []

for url in url_list:
    res = requests.get(url)
    xbeautiful_soup = XBeautifulSoup(BeautifulSoup(res.text, "html.parser"))
    image_tag_list.append(
        FindWebElementsService(BeautifulSoupScraper(xbeautiful_soup)).by_tag_name("a")
    )


# print(url_list)

# base_path = "http://localhost:8023/comm/20180522"
# target_dir = ""
# image_dir_path = base_path + "assets/img/top"
# download_path_from = base_path + target_dir
# res = requests.get(download_path_from)

# xbeautiful_soup = XBeautifulSoup(BeautifulSoup(res.text, "html.parser"))
# image_tag_list: List[WebElement] = FindWebElementsService(
#     BeautifulSoupScraper(xbeautiful_soup)
# ).by_tag_name("a")

image_url_list = []

for image_src_list in image_tag_list:
    for image_src in image_src_list:
        try:
            image_url_list.append(image_src["href"])
        except KeyError:
            print("src属性が見つかりませんでした")
            try:
                image_url_list.append(image_src["data-src"])

            except KeyError:
                image_url_list.append(image_src)
                print("data-src属性が見つかりませんでした")

print(image_url_list)


XCsv().output(
    "C:\\Users\\nishigaki\\Desktop\\atag_list.csv",
    pd.DataFrame(data=image_url_list, columns={"url"}),
)


# XCsv().output(
#     "C:\\Users\\nishigaki\\Desktop\\image_tag_list.csv",
#     pd.DataFrame(data=image_src_list, columns={"ソース"}),
# )

# image_list_df = XCsv().read(
#     filepath="C:\\Users\\nishigaki\\Desktop\\image_url_list.csv",
#     encoding="utf_8_sig",
#     header=0,
# )
# column = "url"
# image_list = image_list_df[column].to_list()

# # public\assets\img\comm
# download_path_to = (
#     # "C:\\Users\\nishigaki\\Desktop\\tavenal-com\\public\\assets\\img\\comm"
#     "C:\\Users\\nishigaki\\Desktop\\downloads\\"
# )

# # 画像URLからダウンロード
# for i, image_url in enumerate(image_list):
#     x_url = XUrl(href=image_url)
#     if CheckIsValidUrlService().execute(x_url):
#         x_image = XImage(x_url=x_url, alt="")
#         DownloadImageService().execute(
#             x_image=x_image, download_path_to=download_path_to, prefix=i + 1
#         )
