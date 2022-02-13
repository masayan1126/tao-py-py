
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.keys import Keys
from shared.Application.find_web_element_service import FindWebElementService
from shared.Application.open_browser_service import OpenBrowserService
from shared.Application.set_webelement_value_service import SetWebElementService
from shared.Domain.Converter.data_frame_converter import DataFrameConverter
from shared.Domain.Scraping.selenium_scraper import SeleniumScraper
from shared.Domain.xbrowser import XBrowser
from shared.Domain.xdriver import XDriver
from shared.Domain.xexcel import XExcel
from shared.Domain.xurl import XUrl
from shared.Domain.xweb_element import XWebElement
from shared.Domain.xweb_element_list import XWebElementList
from shared.Enums.SiteType import SiteType
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# 自動起動したいサイトのurlやログイン情報を記載したエクセルを読み込み -------------------------------------------------------------------------------
subscribe_list_filepath = (
    "C:\\Users\\nishigaki\\jupyter-lab\\packages\\daily_subscribe\\subscribe_list.xlsx"
)
subscribe_wb = XExcel().read(filepath=subscribe_list_filepath, sheet_name=None)
subscribe_sheet = subscribe_wb.get_sheet_by_name("subscribe_list")
subscribe_records = subscribe_sheet.get_records(0, 100, 0, 10)
subscribe_list = DataFrameConverter.to_dictionary(subscribe_records)

if len(subscribe_list) == 0:
    sys.exit()

# ブラウザ起動準備 ---------------------------------------------------------------------------------------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_experimental_option("detach", True)  # 処理完了後もブラウザが起動している状態を保持する
chrome_service = fs.Service(executable_path=ChromeDriverManager().install())
xdriver = XDriver(chrome_service, chrome_options, "Chrome")

# エクセルの内容をもとに、ブラウザ起動
for subscribe in subscribe_list:
    driver = OpenBrowserService().execute(xbrowser=XBrowser(xdriver, XUrl(subscribe["url"])), needs_multiple_tags=False)

    # ブラウザで起動するサイトの種別に応じてmatch～case文で処理
    match SiteType(subscribe["site_type"]):
        case SiteType.NEEDS_LOGIN_AND_TWO_STEP:
            xweb_element_list = XWebElementList(web_elements=[
                # user_id
                XWebElement(
                    FindWebElementService(SeleniumScraper(driver=driver)).find_element_by_id(
                        subscribe["user_id_elem"]),
                    subscribe["user_id"]
                ),
            ])

            SetWebElementService().execute(xweb_element_list)
            FindWebElementService(SeleniumScraper(driver=driver)).find_element_by_xpath(
                subscribe["submit_elem"]).click()

            sleep(1)

            xweb_element_list = XWebElementList(web_elements=[
                # user_password
                XWebElement(
                    FindWebElementService(SeleniumScraper(driver=driver)).find_element_by_id(
                        subscribe["pass_elem"]
                    ),
                    subscribe["password"],
                )
            ])

            # パスワード入力後サブミットボタン
            SetWebElementService().execute(xweb_element_list)

            # TODO: 固定になっている
            xweb_element_list.get_web_element_list()[0].get_element().send_keys(Keys.ENTER)

        case SiteType.NEEDS_LOGIN_AND_ONE_STEP:
            xweb_element_list = XWebElementList(web_elements=[
                # user_id
                XWebElement(
                    FindWebElementService(SeleniumScraper(driver=driver)).find_element_by_id(
                        subscribe["user_id_elem"]
                    ),
                    subscribe["user_id"],
                ),
                # user_password
                XWebElement(
                    FindWebElementService(SeleniumScraper(driver=driver)).find_element_by_id(
                        subscribe["pass_elem"]
                    ),
                    subscribe["password"],
                )
            ])
           
            SetWebElementService().execute(xweb_element_list)
            FindWebElementService(SeleniumScraper(driver=driver)).find_element_by_xpath(
                subscribe["submit_elem"]
            ).click()
        case _:
            pass
        
