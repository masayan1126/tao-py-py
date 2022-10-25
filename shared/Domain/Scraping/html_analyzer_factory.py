from bs4 import BeautifulSoup
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer
from shared.Core.di_container import DiContainer
from shared.Core.factory import Factory
from shared.Domain.Url.x_url import XUrl
import requests


class HtmlAnalyzerFactory(Factory):
    def create(self, xurl: XUrl, cookie: dict = None) -> HtmlAnalyzer:

        if cookie:
            session = requests.session()
            session.get(xurl.url())

            res = requests.get(xurl.url(), cookies=cookie)

        else:
            res = requests.get(xurl.url())

        html_analyzer: HtmlAnalyzer = DiContainer().resolve(HtmlAnalyzer)
        html_analyzer.bind(beautiful_soup=BeautifulSoup(res.content, "html.parser"))
        return html_analyzer
