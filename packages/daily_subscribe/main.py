import sys
from packages.daily_subscribe.env import ENV
from shared.Application.Init.initializer import Initializer
from shared.Domain.Converter.data_frame_converter import DataFrameConverter
from shared.Domain.Excel.xexcel import XExcel
from shared.Enums.site_type import SiteType
from shared.di_container import DiContainer
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.Domain.xurl import XUrl
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.Enums.browser_type import BrowserType
from shared.i_factory import IFactory
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import SessionNotCreatedException
from shared.x_logger import XLogger


Initializer().ioOption()

# 自動起動したいサイトのurlやログイン情報を記載したエクセルを読み込み -------------------------------------------------------------------------------
subscribe_list_filepath = (
    "C:\\Users\\nishigaki\\jupyter-lab\\packages\\daily_subscribe\\subscribe_list.xlsx"
)
subscribe_wb = XExcel().read(filepath=subscribe_list_filepath, sheet_name=None)
subscribe_sheet = subscribe_wb.get_sheet_by_name("subscribe_list")
subscribe_records = subscribe_sheet.get_records(0, 100, 0, 10)
subscribe_list = DataFrameConverter.to_dictionary(subscribe_records)

# TODO: コンバートするクラスでチェックするようにする
if len(subscribe_list) == 0:
    sys.exit()

# 1.ブラウザ起動 ---------------------------------------------------------------------------------------------------
try:
    xdriver_factory: IFactory = XDriverFactory()
except SessionNotCreatedException as e:
    XLogger.exception_to_slack(
        ENV["SLACK_WEBHOOK_URL_JOBCAN"],
        "webdriverのバージョンがChromeブラウザーのバージョンと一致していないため起動に失敗しました。"
    )

xdriver = xdriver_factory.create(BrowserType.CHROME, is_headless=False)
xbrowser_factory: IFactory = XBrowserFactory()
i_web_browser_operator: IWebBrowserOperator = DiContainer().resolve(IWebBrowserOperator)


# エクセルの内容をもとに、ブラウザ起動
for subscribe in subscribe_list:
    # ブラウザで起動するサイトの種別に応じてmatch～case文で処理
    match SiteType(subscribe["site_type"]):
        case SiteType.NEEDS_LOGIN_AND_TWO_STEP:
            xbrowser = xbrowser_factory.create(xdriver, XUrl(subscribe["url"]))
            i_web_browser_operator.boot(xbrowser)
            
            sleep(1)
            user_id = i_web_browser_operator.find_by_id(subscribe["user_id_elem"])
            
            i_web_browser_operator.send_value(
                XWebElementList(
                    [
                        user_id.set_value(subscribe["user_id"]),
                    ]
                )
            )

            i_web_browser_operator.find_by_xpath(subscribe["submit_elem"]).web_element().click()
            sleep(1)

            password = i_web_browser_operator.find_by_id(subscribe["pass_elem"])
            i_web_browser_operator.send_value(XWebElementList([password.set_value(subscribe["password"])]))
            password.web_element().send_keys(Keys.ENTER)

        case SiteType.NEEDS_LOGIN_AND_ONE_STEP:

            xbrowser = xbrowser_factory.create(xdriver, XUrl(subscribe["url"]))
            i_web_browser_operator.boot(xbrowser)
            
            sleep(1)
            user_id = i_web_browser_operator.find_by_id(subscribe["user_id_elem"])
            
            i_web_browser_operator.send_value(
                XWebElementList(
                    [
                        user_id.set_value(subscribe["user_id"]),
                    ]
                )
            )


            password = i_web_browser_operator.find_by_id(subscribe["pass_elem"])
            i_web_browser_operator.send_value(XWebElementList([password.set_value(subscribe["password"])]))
            # password.web_element().send_keys(Keys.ENTER)

            i_web_browser_operator.find_by_xpath(subscribe["submit_elem"]).web_element().click()
            sleep(1)
        case _:
            pass
