from dataclasses import dataclass
from shared.Domain.Wp.wp_operator import WpOperator
import requests
from shared.Domain.Url.x_url import XUrl
import json
from shared.Domain.Wp.post import Post


@dataclass
class WpOperatorImpl(WpOperator):
    api_url: XUrl

    def response_headers(self):
        return requests.head(self.api_url.href()).headers

    def total_page_count(self) -> int:
        return int(self.response_headers()["X-WP-TotalPages"])

    def total_posts_count(self) -> int:
        return int(self.response_headers()["X-WP-Total"])

    def fetch_posts(self, page: int = None) -> list[Post]:
        posts = []

        # ページ指定なし
        if page is None:
            _posts = []
            for page in range(1, self.total_page_count() + 1):
                res = requests.get(f"{self.api_url.href()}?page={page}")

                for post in json.loads(res.text):
                    _posts.append(post)  # JSON文字列を辞書型に変換

        else:
            res = requests.get(f"{self.api_url.href()}?page={page}")
            _posts = json.loads(res.text)

        for post in _posts:
            posts.append(
                Post(
                    post["id"], post["status"], post["link"], post["title"]["rendered"]
                )
            )
        return posts
