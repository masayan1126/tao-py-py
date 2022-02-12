from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
import pytest
from shared.Application.open_browser_service import OpenBrowserService
from shared.Domain.xbrowser import XBrowser
from shared.Domain.xdriver import XDriver
from shared.Domain.xurl import XUrl
from shared.Domain.xweb_element import XWebElement


@pytest.fixture
def setuped_chrome_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_experimental_option("detach", True)  # 処理完了後もブラウザが起動している状態を保持する
    # options.add_argument('--headless')
    chrome_service = fs.Service(executable_path=ChromeDriverManager().install())
    xdriver = XDriver(chrome_service, chrome_options, "Chrome")
    return OpenBrowserService().execute(
        xbrowser=XBrowser(xdriver, XUrl("https://maasaablog.com/")),
        needs_multiple_tags=False,
    )


def test_対象のページからhtml要素を取得できること(setuped_chrome_browser):
    xweb_element = XWebElement(
        setuped_chrome_browser.find_element_by_id("menu-menu-1"),
        "",
    )

    assert xweb_element.get_value() == ""
