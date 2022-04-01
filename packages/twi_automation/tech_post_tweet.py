import sys
from twitter_operator import TwitterOperator
import json
import requests

tweet_content = ""

# WordPressページ数取得(パラメータ設定)
url = "https://maasaablog.com/"
endpoint = '/wp-json/wp/v2/posts'
api_url = url + endpoint
page_count = 100

# res = requests.get(f"{api_url}?page=2").json()
response_headers = requests.head(api_url).headers

total_page_count = int(response_headers['X-WP-TotalPages'])
total_posts_count = int(response_headers["X-WP-Total"])

# TODO: pandasでcsv出力する(これは別スクリプトで1ヶ月に一回くらいcronで定期実行して所定のパスにおく or dbに保存)
# for page_count in range(1, total_page_count + 1):
#     res = requests.get(f"{api_url}?page={page_count}")
#     posts = json.loads(res.text)
    
#     for post in posts:
#         post_info = {"title": post["title"]["rendered"], "link":post["link"]}
#         print(post_info)

# TODO: pandasでcsvを読み取り、そのlinkをもとにtwitterにシェアする
# 30分おきにランダムで1記事をツイートできるようにする


# 読み取ったdataframeサンプル
posts = [
    {"title": "Visual Studio CodeでPythonスクリプトを効率的にデバッグする方法", "link": "https://maasaablog.com/development/python/4357/"},
    {"title": "VsCodeでマークダウンファイル(.md)を快適に使用するTips", "link": "https://maasaablog.com/tools/visual-studio-code/1762/"},
]


for post in posts:
    title = post["title"]
    link = post["link"]
    tweet_content = f"{title}""\n\n"f"{link}"
    twitter_operator = TwitterOperator()
    twitter_operator.tweet(tweet_content)