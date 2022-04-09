from shared.Domain.Excel.xcsv import XCsv
from shared.Domain.Wp.wp_operator import WpOperator

# 毎月1日10::00に実行して新規記事を取り込む

url = "https://maasaablog.com/"
endpoint = "/wp-json/wp/v2/posts"
api_url = url + endpoint

wp = WpOperator(api_url=api_url)
posts = wp.fetch_posts()

XCsv().output(
    "C:\\Users\\nishigaki\\jupyter-lab\\packages\\twi_automation\\posts.csv", posts
)
