from dataclasses import dataclass
from urllib.parse import urlparse
from urllib.parse import urljoin
import urllib.request, urllib.error
from retry import retry

# URLを6つの構成要素に分解(返り値は6つの構成要素のタプル)
# [scheme]:// [netloc] / [path] ; [parameters] ? [query] # [fragment]


@dataclass
class XUrl:
    @retry(exceptions=(urllib.error.HTTPError), tries=10)
    def __init__(self, encoded_href: str):
        self._href = encoded_href

    def href(self) -> str:
        return self._href

    def scheme(self) -> str:
        return urlparse(self.href()).scheme

    def netloc(self) -> str:
        return urlparse(self.href()).netloc

    def path(self) -> str:
        return urlparse(self.href()).path

    def query_params(self) -> str:
        return urlparse(self.href()).query

    def fragment(self) -> str:
        return urlparse(self.href()).fragment

    # 基底URLを返します
    def baseurl(self) -> str:
        return f"{self.scheme()}://{self.netloc()}/"

    def join(self, relative_path: str):
        """基底パスに任意の相対パスを結合したurlを返します

        Args:
            relative_path ([str]): [相対パス]

        Returns:
            joined_url [str]: [基底パスに任意の相対パスを結合したurl]
        """
        return XUrl(urljoin(self.baseurl(), relative_path))
