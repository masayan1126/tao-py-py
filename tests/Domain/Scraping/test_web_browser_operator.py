# from unittest.mock import MagicMock, patch
# from shared.Application.Scraping.chrome_browser_boot_up_usecase import (
#     ChromeBrowserBootUpUsecase,
# )
# from shared.Domain.Scraping.web_browser_factory import WebBrowserFactory
# from shared.Domain.Scraping.web_browser_operator_impl import WebBrowserOperatorImpl
# from shared.Domain.Url.x_url import XUrl
# from shared.Enums.browser_type import BrowserType

# # @pytest.fixture
# # def setuped_web_browser_operator():
# #     factory: Factory = XDriverFactory()
# #     xdriver = factory.create(BrowserType.CHROME, is_headless=True, on_docker=True)

# #     factory: Factory = XBrowserFactory()
# #     xbrowser = factory.create(xdriver, XUrl("https://maasaablog.com/"))

# #     i_web_browser_operator: WebBrowserOperator = DiContainer().resolve(
# #         WebBrowserOperator
# #     )
# #     i_web_browser_operator.boot(xbrowser)

# #     yield i_web_browser_operator

# #     xdriver.driver().quit()


# # @patch("shared.Domain.Scraping.web_browser_operator_impl.WebElement")
# # @patch("shared.Domain.Scraping.web_browser_factory")
# # @patch("shared.Domain.Scraping.x_driver_factory.BrowserJudgement")
# # def test_ID名でhtml要素を取得できること(
# #     chrome_webdriver_mock, chrome_browser_factory_mock, web_element_mock
# # ):
# #     chrome_webdriver_mock.judge.return_value = MagicMock(name="1")

# #     chrome_browser_factory_mock.create.return_value = MagicMock(name="2")

# #     chorme_browser_operator = WebBrowserFactory().create(
# #         BrowserType.CHROME, XUrl("https://maasaablog.com"), False
# #     )

# #     web_element_mock.find_element.return_value = MagicMock(name="3", text="masayanblog")

# #     # # ヘッダメニューのタイトル
# #     actual = chorme_browser_operator.find_by_id("aaaaa").text
# #     expected = "masayanblog"

# #     assert expected == actual


# @patch("shared.Application.Scraping.chrome_browser_boot_up_usecase.WebBrowserOperator")
# @patch("shared.Application.Scraping.chrome_browser_boot_up_usecase.WebBrowserFactory")
# def test_ID名でhtml要素を取得できること(
#     web_browser_factory_create_mock, web_browser_operator_mock
# ) -> None:
#     instance = web_browser_factory_create_mock.return_value

#     web_browser_operator_mock.find
#     instance.create.return_value = web_browser_operator_mock  # web_browser_operator

#     chorme_browser_operator = ChromeBrowserBootUpUsecase(
#         XUrl("https://hogefoovar.com")
#     ).handle()

#     # impl = WebBrowserOperatorImpl()
#     # dummy_web_element = ""
#     # mock_xbrowser = MagicMock()
#     # config = {
#     #     # xdriver().driver().find_element(By.ID, id_name)
#     #     "xdriver.return_value.driver.return_value.find_element.return_value": dummy_web_element
#     # }
#     # mock_xbrowser.configure_mock(**config)

#     # chorme_browser_operator.boot(mock_xbrowser)

#     assert chorme_browser_operator.find_by_id("gegeg") == "masayanblog"


# # def test_xpath名でhtml要素を取得できること(setuped_web_browser_operator: WebBrowserOperator):
# #     # ヘッダメニューのタイトル
# #     actual = (
# #         setuped_web_browser_operator.find_by_xpath("//*[@id='header-in']/h1/a/span")
# #         .web_element()
# #         .text
# #     )
# #     expected = "masayanblog"

# #     assert expected == actual
