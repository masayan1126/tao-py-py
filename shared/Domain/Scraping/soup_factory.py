from bs4 import BeautifulSoup
from shared.i_factory import IFactory
from shared.Domain.xurl import XUrl
import requests


class SoupFactory(IFactory):
    def create(self, xurl: XUrl) -> BeautifulSoup:
        res = requests.get(xurl.get_href())
        return BeautifulSoup(res.text, "html.parser")