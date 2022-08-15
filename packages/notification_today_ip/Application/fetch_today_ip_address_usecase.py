from dataclasses import dataclass
from shared.Domain.Scraping.i_html_analyzer import IHtmlAnalyzer
from shared.Domain.String.ip_address import IpAddress
from shared.Domain.String.ip_address_service import IpAddressService


@dataclass
class FetchTodayIpAddressUsecase:
    i_html_analyzer: IHtmlAnalyzer

    def fetch(self) -> IpAddress:

        try:
            return IpAddressService(self.i_html_analyzer).today_ip()

        except Exception as e:
            raise e
