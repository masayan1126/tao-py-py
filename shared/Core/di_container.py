import injector
from shared.Domain.Scraping.html_analyzer_impl import HtmlAnalyzerImpl
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer


class DiContainer:
    def mappings(self, binder) -> None:
        # binder.bind(
        #     WebBrowserOperator, to=injector.InstanceProvider(WebBrowserOperatorImpl())
        # )
        binder.bind(HtmlAnalyzer, to=injector.InstanceProvider(HtmlAnalyzerImpl()))

        # TODO: wp,textfile,twi,automatic,calendar,SoftWareProcessOperator

    # 引数にinterfaceを実現したクラスをmappingsをもとに返します
    def resolve(self, c):
        return injector.Injector(self.mappings).get(c)
