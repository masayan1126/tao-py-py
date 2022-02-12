from urllib.parse import urlparse
from urllib.parse import urljoin

# URLを6つの構成要素に分解(返り値は6つの構成要素のタプル)
# [scheme]:// [netloc] / [path] ; [parameters] ? [query] # [fragment]
class XUrl:
    def __init__(self, href: str):
        self.href = href

    def get_href(self):
        return self.href

    def get_scheme(self):
        return urlparse(self.href).scheme

    def get_netloc(self):
        return urlparse(self.href).netloc

    def get_path(self):
        return urlparse(self.href).path

    def get_params(self):
        return urlparse(self.href).params

    def get_query(self):
        return urlparse(self.href).query

    def get_fragment(self):
        return urlparse(self.href).fragment

    # 基底URLを返します
    def get_baseurl(self):
        return f"{self.get_scheme()}://{self.get_netloc()}/"

    def join_to(self, relative_path) -> str:
        """基底パスに任意の相対パスを結合したurlを返します

        Args:
            relative_path ([str]): [相対パス]

        Returns:
            joined_url [str]: [基底パスに任意の相対パスを結合したurl]
        """
        return urljoin(self.get_baseurl(), relative_path)
