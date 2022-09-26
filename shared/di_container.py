import injector
from shared.Domain.Scraping.html_analyzer_impl import HtmlAnalyzerImpl
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer

from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator


class DiContainer:
    def mappings(self, binder) -> None:
        binder.bind(
            IWebBrowserOperator, to=injector.InstanceProvider(WebBrowserOperator())
        )
        binder.bind(HtmlAnalyzer, to=injector.InstanceProvider(HtmlAnalyzerImpl()))

    def resolve(self, c):
        return injector.Injector(self.mappings).get(c)
