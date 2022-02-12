import io, sys, os, signal
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from shared.Domain.xurl import XUrl

from shared.Domain.xweb_element import XWebElement
from shared.Domain.xdriver import XDriver
from shared.Application.open_text_service import OpenTextService
from shared.Domain.xbrowser import XBrowser
from shared.Application.open_browser_service import OpenBrowserService
from shared.Domain.xtext import XText
from shared.Application.set_webelement_value_service import SetWebElementService

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# ログインパスワードを取得 -------------------------------------------------------------------------------
# TODO:OSの環境変数に追加してそれを使うようにする
password_filepath = "C:\\Users\\nishigaki\\jupyter-lab\\password.txt"
password = OpenTextService().execute(
    x_text=XText(password_filepath), mode="r", encoding="UTF-8"
)

if password == "":
    sys.exit()
    # プロセスをkill
    # os.kill(driver.service.process.pid, signal.SIGTERM)

# ブラウザ起動 ---------------------------------------------------------------------------------------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_experimental_option("detach", True)  # 処理完了後もブラウザが起動している状態を保持する
# options.add_argument('--headless')
chrome_service = fs.Service(executable_path=ChromeDriverManager().install())
xdriver = XDriver(chrome_service, chrome_options, "Chrome")
chrome_driver = xdriver.get_scraper()
chrome_browser = OpenBrowserService().execute(
    xbrowser=XBrowser(chrome_driver, XUrl("https://id.jobcan.jp/")),
    needs_multiple_tags=False,
)

# htmlを取得し値をセットして送信 -----------------------------------------------------------------------------------
# TODO:emailも外から渡すようにする
user_email = XWebElement(
    "user_email",
    chrome_browser.find_element_by_id("user_email"),
    "nishigaki@aivick.co.jp",
)
user_password = XWebElement(
    "user_password",
    chrome_browser.find_element_by_id("user_password"),
    password,
)
SetWebElementService().execute([user_email, user_password])
chrome_browser.find_element_by_xpath("//*[@id='new_user']/input[2]").click()

# 処理後、ブラウザを閉じる場合は以下
# chrome_browser.get_browser_object().quit()
