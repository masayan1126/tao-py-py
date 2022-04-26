from typing import Dict
from bs4 import BeautifulSoup
from shared.i_factory import IFactory
from shared.Domain.Url.x_url import XUrl
import requests


class SoupFactory(IFactory):
    def create(self, xurl: XUrl, cookie: Dict = None) -> BeautifulSoup:

        if cookie:
            session = requests.session()
            session.get(xurl.href())

            return BeautifulSoup(
                requests.get(xurl.href(), cookies=cookie).content, "html"
            )
        else:
            res = requests.get(xurl.href())
            return BeautifulSoup(res.text, "html.parser")
