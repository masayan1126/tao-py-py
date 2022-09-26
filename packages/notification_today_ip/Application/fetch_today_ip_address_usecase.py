from dataclasses import dataclass
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer
from shared.Domain.String.ip_address import IpAddress
from shared.Domain.String.ip_address_service import IpAddressService


@dataclass
class FetchTodayIpAddressUsecase:
    html_analyzer: HtmlAnalyzer

    def fetch(self) -> IpAddress:

        try:
            return IpAddressService(self.html_analyzer).today_ip()

        except Exception as e:
            raise e
