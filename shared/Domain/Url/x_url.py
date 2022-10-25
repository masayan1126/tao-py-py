from dataclasses import dataclass
from urllib.parse import urlparse
from urllib.parse import urljoin
import urllib.request, urllib.error
from retry import retry
import urllib.parse


@dataclass
class XUrl:
    """インスタンス生成時のドメインルール
    - URLを6つの構成要素に分解(返り値は6つの構成要素のタプル)
    - [scheme]:// [netloc] / [path] ; [parameters] ? [query] # [fragment]
    """

    @retry(exceptions=(urllib.error.HTTPError), tries=10)
    def __init__(self, url: str):
        self._url = url

    def url(self) -> str:
        return self._url

    def scheme(self) -> str:
        return urlparse(self.url()).scheme

    def netloc(self) -> str:
        return urlparse(self.url()).netloc

    def path(self) -> str:
        return urlparse(self.url()).path

    def query_params(self) -> str:
        return urlparse(self.url()).query

    def fragment(self) -> str:
        return urlparse(self.url()).fragment

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

    # def decode(self) -> str:
    #     return urllib.parse.unquote(self.url())

    # def encode(self) -> str:
    # not_escape_ascii = "/?:#="
    #     return urllib.parse.quote(self.url(), safe="")
