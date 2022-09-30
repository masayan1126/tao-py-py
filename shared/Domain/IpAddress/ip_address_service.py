# from __future__ import annotations
from dataclasses import dataclass
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer
from shared.Domain.IpAddress.ip_address import IpAddress


@dataclass
class IpAddressService:
    html_analyzer: HtmlAnalyzer
    # def __init__(self, html_analyzer: HtmlAnalyzer):
    #     self.html_analyzer = html_analyzer

    def get_today_ip(self) -> IpAddress:
        today_ip_address = self.html_analyzer.search_by_selector("font")[1].text
        return IpAddress(today_ip_address)
