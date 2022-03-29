from typing import Callable, Type, TypeVar
import injector
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer
from shared.Domain.Scraping.i_html_analyzer import IHtmlAnalyzer

from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator


class DiContainer:
    def mappings(self, binder)->None:
        binder.bind(
            IWebBrowserOperator, to=injector.InstanceProvider(WebBrowserOperator())
        )
        binder.bind(IHtmlAnalyzer, to=injector.InstanceProvider(HtmlAnalyzer()))

    def resolve(self, c):
        return injector.Injector(self.mappings).get(c)
