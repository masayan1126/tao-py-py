from glob import glob
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.Domain.Url.x_url import XUrl
from shared.Application.Init.initializer import Initializer
from shared.di_container import DiContainer
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.Domain.Url.x_url import XUrl
from shared.Enums.browser_type import BrowserType

Initializer().ioOption()

# ブラウザ起動 ---------------------------------------------------------------------------------------------------
xdriver = XDriverFactory().create(BrowserType.CHROME, is_headless=False)
xbrowser = XBrowserFactory().create(xdriver, XUrl("https://tinyjpg.com/"))
i_web_browser_operator: IWebBrowserOperator = DiContainer().resolve(IWebBrowserOperator)
i_web_browser_operator.boot(xbrowser)

# 画像アップロード -----------------------------------------------------------------------------------
image_file_list = glob("./images/*.*")

for image in image_file_list:

    i_web_browser_operator.send_value(
        XWebElementList(
            [
                i_web_browser_operator.find_by_xpath(
                    xpath="//*[@id='top']/section/div[1]/section/input"
                ).set_value(image)
            ]
        )
    )
