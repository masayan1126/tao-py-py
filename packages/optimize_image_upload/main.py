import io, sys
from glob import glob
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from shared.Domain.xurl import XUrl

from shared.Domain.xweb_element import XWebElement
from shared.Domain.xdriver import XDriver
from shared.Domain.xbrowser import XBrowser
from shared.Application.open_browser_service import OpenBrowserService
from shared.Application.set_webelement_service import SetWebElementService

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# ブラウザ起動 ---------------------------------------------------------------------------------------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_experimental_option("detach", True)  # 処理完了後もブラウザが起動している状態を保持する
# options.add_argument('--headless')
chrome_service = fs.Service(executable_path=ChromeDriverManager().install())
xdriver = XDriver(chrome_service, chrome_options, "Chrome")
chrome_driver = xdriver.get_scraper()
chrome_browser = OpenBrowserService().execute(
    browser=XBrowser(chrome_driver, XUrl("https://tinyjpg.com/"))
)

# 画像アップロード -----------------------------------------------------------------------------------
image_file_list = glob(
    "C:\\Users\\nishigaki\\jupyter-lab\\packages\\optimize_image_upload\\images\\*.*"
)

upload_element_list = []

for image in image_file_list:
    upload_area_element = XWebElement(
        "",
        chrome_browser.find_element_by_xpath(
            "//*[@id='top']/section/div[1]/section/input"
        ),
        image,
    )

    upload_element_list.append(upload_area_element)

SetWebElementService().execute(upload_element_list)
