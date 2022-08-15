from dataclasses import dataclass
from shared.Domain.Scraping.i_html_analyzer import IHtmlAnalyzer
from shared.Domain.String.ip_address import IpAddress


@dataclass
class IpAddressService:
    i_html_analyzer: IHtmlAnalyzer

    def today_ip(self) -> IpAddress:
        today_ip_address = self.i_html_analyzer.search_by_selector("font")[1].text
        return IpAddress(today_ip_address)
