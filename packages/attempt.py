from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer
from shared.Domain.Scraping.soup_factory import SoupFactory
from shared.Domain.Url.x_url import XUrl
from shared.di_container import DiContainer
from shared.factory import Factory
from shared.Domain.IpAddress.ip_address_service import IpAddressService


site_url = "https://www.ugtop.com/spill.shtml"
factory: Factory = SoupFactory()
soup = factory.create(XUrl(site_url))
html_analyzer: HtmlAnalyzer = DiContainer().resolve(HtmlAnalyzer)
html_analyzer.bind(soup)
ip_address = IpAddressService(html_analyzer).get_today_ip()

print(ip_address.value())
