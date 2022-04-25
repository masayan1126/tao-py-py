from typing import Dict
from bs4 import BeautifulSoup
from shared.i_factory import IFactory
from shared.Domain.xurl import XUrl
import requests


class SoupFactory(IFactory):
    def create(self, xurl: XUrl, cookie: Dict = None) -> BeautifulSoup:

        if cookie:
            session = requests.session()
            session.get(xurl.get_href())

            return BeautifulSoup(
                requests.get(xurl.get_href(), cookies=cookie).content, "html"
            )
        else:
            res = requests.get(xurl.get_href())
            return BeautifulSoup(res.text, "html.parser")
