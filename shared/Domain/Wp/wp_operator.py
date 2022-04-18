from typing import List

import urllib.request, urllib.error
from shared.Domain.Wp.i_wp_operator import IWpOperator
import requests
from shared.Domain.xurl import XUrl
import json
from shared.Exception.wp_error import WpError


class WpOperator(IWpOperator):
    def __init__(self, api_url: XUrl):
        # urlがそもそも無効ならここで落とす

        try:
            f = urllib.request.urlopen(api_url)
            self._api_url = api_url
        except urllib.error.URLError as e:
            raise e
        finally:
            if "f" in locals():
                f.close()

    def response_headers(self):
        return requests.head(self._api_url).headers

    def total_page_count(self) -> int:
        try:
            return int(self.response_headers()["X-WP-TotalPages"])
        except KeyError as e:
            raise WpError("This url is valid. But may not be a wordpress api url")

    def total_posts_count(self) -> int:
        try:
            return int(self.response_headers()["X-WP-Total"])
        except KeyError as e:
            raise WpError("This url is valid. But may not be a wordpress api url")

    def fetch_posts(self, page_number: int = None) -> List[dict]:
        try:
            posts = []

            # ページ指定なし
            if page_number is None:
                _posts = []
                for page_count in range(1, self.total_page_count() + 1):
                    res = requests.get(f"{self._api_url}?page={page_count}")

                    for post in json.loads(res.text):
                        _posts.append(post)  # JSON文字列を辞書型に変換

            else:
                res = requests.get(f"{self._api_url}?page={page_number}")
                _posts = json.loads(res.text)  # JSON文字列を辞書型に変換

            for post in _posts:

                post_info = {
                    "title": post["title"]["rendered"],
                    "link": post["link"],
                }
                posts.append(post_info)
            return posts

        except requests.exceptions.HTTPError as e:
            raise e
