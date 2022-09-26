from dataclasses import dataclass
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer
from shared.Domain.String.ip_address import IpAddress


@dataclass
class IpAddressService:
    html_analyzer: HtmlAnalyzer

    def today_ip(self) -> IpAddress:
        today_ip_address = self.html_analyzer.search_by_selector("font")[1].text
        return IpAddress(today_ip_address)
