from dataclasses import dataclass
from packages.today_task_notification.env import ENV
from shared.Domain.Log.x_logger import XLogger
from shared.Domain.Scraping.i_html_analyzer import IHtmlAnalyzer
from shared.Domain.String.ip_address import IpAddress
from time import sleep
from shared.Domain.Scraping.i_html_analyzer import IHtmlAnalyzer
from shared.Domain.Scraping.soup_factory import SoupFactory
from shared.Domain.String.ip_address_service import IpAddressService
from shared.Domain.Url.x_url import XUrl
from shared.di_container import DiContainer
from selenium.common.exceptions import SessionNotCreatedException

from shared.i_factory import IFactory


@dataclass
class FetchTodayIpAddressUsecase:
    i_html_analyzer: IHtmlAnalyzer

    def fetch(self) -> IpAddress:

        try:
            return IpAddressService(self.i_html_analyzer).today_ip()

        except SessionNotCreatedException as e:
            raise e
