from bs4 import BeautifulSoup
from shared.factory import Factory
from shared.Domain.Url.x_url import XUrl
import requests


class SoupFactory(Factory):
    def create(self, xurl: XUrl, cookie: dict = None) -> BeautifulSoup:

        if cookie:
            session = requests.session()
            session.get(xurl.href())

            return BeautifulSoup(
                requests.get(xurl.href(), cookies=cookie).content, "html"
            )
        else:
            res = requests.get(xurl.href())

            return BeautifulSoup(res.content, "html.parser")
