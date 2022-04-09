from typing import List
from shared.Domain.Wp.i_wp_operator import IWpOperator
import requests
from shared.Domain.xurl import XUrl
import json


class WpOperator(IWpOperator):
    def __init__(self, api_url: XUrl):
        self._api_url = api_url

    def response_headers(self):
        return requests.head(self._api_url).headers

    def total_page_count(self) -> int:
        return int(self.response_headers()["X-WP-TotalPages"])

    def total_posts_count(self) -> int:
        return int(self.response_headers()["X-WP-Total"])

    def fetch_posts(self, page_number: int = None) -> List[dict]:
        try:
            # page_query = f"?page={page}"
            # res = requests.get(f"{self._api_url}{page_query}").json()
            posts = []

            # ページ指定なし
            if page_number is None:
                # TODO: pandasでcsv出力する(これは別スクリプトで1ヶ月に一回くらいcronで定期実行して所定のパスにおく or dbに保存)
                for page_count in range(1, self.total_page_count() + 1):
                    res = requests.get(f"{self._api_url}?page={page_count}")
                    _posts = json.loads(res.text)

                    for post in _posts:
                        post_info = {
                            "title": post["title"]["rendered"],
                            "link": post["link"],
                        }
                        posts.append(post_info)

            else:
                res = requests.get(f"{self._api_url}?page={page_number}")
                _posts = json.loads(res.text)

                for post in _posts:
                    post_info = {
                        "title": post["title"]["rendered"],
                        "link": post["link"],
                    }
                    posts.append(post_info)

            return posts

        except Exception as e:
            # FIXME: エラーハンドリング(ただしこのクラスではraiseするだけ)
            raise e

            # if 32 in e.api_codes:
            #     logger.exception(
            #         "認証に失敗しました。\n認証情報はこちらから確認できます(https://developer.twitter.com/en/portal/dashboard)"
            #     )
            # elif 187 in e.api_codes:
            #     logger.exception("重複するツイートが投稿されました。")
            # else:
            #     logger.exception(e)
