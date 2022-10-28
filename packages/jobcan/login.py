from packages.jobcan.Application.jobcan_login_usecase import JobcanLoginUsecase
from shared.Domain.Scraping.browser_type import BrowserType
from shared.Domain.Scraping.web_browser_operator_factory import (
    WebBrowserOperatorFactory,
)
from shared.Domain.Url.x_url import XUrl

chorme_browser_operator = WebBrowserOperatorFactory().create(
    x_url=XUrl("https://id.jobcan.jp/"),
    browser_type=BrowserType.CHROME,
)

JobcanLoginUsecase(chorme_browser_operator).login()
