from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Application.Init.initializer import Initializer
from shared.Domain.xurl import XUrl
import pytest
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.Enums.browser_type import BrowserType
from shared.Domain.Scraping.x_browser_factory import XBrowserFactory
from shared.Domain.Scraping.x_driver_factory import XDriverFactory
from shared.i_factory import IFactory
from shared.di_container import DiContainer


@pytest.fixture
def setuped_i_web_browser_operator():
    factory: IFactory = XDriverFactory()
    xdriver = factory.create(BrowserType.CHROME)

    factory: IFactory = XBrowserFactory()
    xbrowser = factory.create(xdriver, XUrl("https://maasaablog.com/"))

    i_web_browser_operator: IWebBrowserOperator = DiContainer().resolve(
        IWebBrowserOperator
    )
    i_web_browser_operator.boot(xbrowser)

    return i_web_browser_operator


def test_ID名でhtml要素を取得できること(setuped_i_web_browser_operator: IWebBrowserOperator):
    # ヘッダメニューのタイトル
    acutual = setuped_i_web_browser_operator.find_by_id("header-in").web_element().text
    excepted = "masayanblog"

    assert acutual == excepted


def test_xpath名でhtml要素を取得できること(setuped_i_web_browser_operator: IWebBrowserOperator):
    # ヘッダメニューのタイトル
    acutual = (
        setuped_i_web_browser_operator.find_by_xpath("//*[@id='header-in']/h1/a/span")
        .web_element()
        .text
    )
    excepted = "masayanblog"

    assert acutual == excepted


# def test_タグ名で全要素を取得できること(setuped_driver):
#     web_element_list = FindWebElementsService(
#         SeleniumScraper(driver=setuped_driver)
#     ).by_tag_name("h1")

#     x_web_element_list_1 = WebElementConverter.convert(web_element_list)
#     x_web_element_list_2 = XWebElementList(web_elements=[])

#     x_web_element_list_2.add(
#         XWebElement(
#             web_element_list[0],
#             "",
#         )
#     )

#     assert x_web_element_list_1 == x_web_element_list_2


# def test_タグ名で全要素を取得できること_bs():

#     res = requests.get("https://maasaablog.com/")
#     xbeautiful_soup = XBeautifulSoup(BeautifulSoup(res.text, "html.parser"))

#     elems = FindWebElementsService(
#         BeautifulSoupScraper(xbeautiful_soup=xbeautiful_soup)
#     ).by_tag_name("h1")

#     assert elems[0].text == "masayanblog"


# def test_クラス名で全要素を取得できること(setuped_driver):
#     elems = FindWebElementsService(
#         SeleniumScraper(driver=setuped_driver)
#     ).by_class_name("logo-text")

#     assert elems[0].text == "masayanblog"
#     # assert type(elems) == "masayanblog"


# def test_name属性で全要素を取得できること(setuped_driver):
#     # 例) <input name="s" placeholder="サイト内を検索" />
#     elems = FindWebElementsService(SeleniumScraper(driver=setuped_driver)).by_attr_name(
#         "s"
#     )

#     elem: WebElement = elems[0]
#     assert elem.get_property("placeholder") == "サイト内を検索"


# def test_xpathで全要素を取得できること(setuped_driver):
#     elems = FindWebElementsService(SeleniumScraper(driver=setuped_driver)).by_xpath(
#         "//*[@id='header-in']/h1"
#     )

#     assert elems[0].text == "masayanblog"


# def test_cssセレクタで全要素を取得できること(setuped_driver):
#     elems = FindWebElementsService(SeleniumScraper(driver=setuped_driver)).by_selector(
#         ".logo-text"
#     )

#     assert elems[0].text == "masayanblog"
