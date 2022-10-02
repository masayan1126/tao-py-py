from shared.Domain.Scraping.web_browser_factory import WebBrowserFactory
from shared.Domain.Url.x_url import XUrl
from shared.Domain.Scraping.browser_type import BrowserType


chorme_browser_operator = WebBrowserFactory().create(
    BrowserType.CHROME, XUrl("https://maasaablog.com"), False
)
