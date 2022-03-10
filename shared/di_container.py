from typing import Callable, Type, TypeVar
import injector

from shared.Domain.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.web_browser_operator import WebBrowserOperator


class DiContainer:
    def mappings(self, binder):
        return binder.bind(
            IWebBrowserOperator, to=injector.InstanceProvider(WebBrowserOperator())
        )

    def resolve(self, c):
        return injector.Injector(self.mappings).get(c)
