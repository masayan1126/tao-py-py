from beautifulsoup4 import BeautifulSoup
import requests
import datetime
from dateutil.relativedelta import relativedelta

URL = "https://maasaablog.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html")
tag = soup.select(selector=".logo > a > span")[0]
print(tag.text)

# timezoneを指定するとdatetimeの生成が早くなる
t_delta = datetime.timedelta(hours=9)
# 日本標準時
jst = datetime.timezone(t_delta, "JST")
now = datetime.datetime.now(jst).isoformat()

with open(f"{now}_log.txt", "w") as f:
    print(tag.text, file=f)
