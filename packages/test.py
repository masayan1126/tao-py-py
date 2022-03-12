from shared.Domain.Scraping.i_html_analyzer import IHtmlAnalyzer
from shared.Domain.Scraping.soup_factory import SoupFactory
from shared.Domain.xurl import XUrl
from shared.di_container import DiContainer

soup = SoupFactory().create(XUrl("https://maasaablog.com/"))
i_html_analyzer: IHtmlAnalyzer = DiContainer().resolve(IHtmlAnalyzer)
i_html_analyzer.bind(soup)

result_set = i_html_analyzer.find_by_id(css_selector="#sidebar")
print(result_set)
