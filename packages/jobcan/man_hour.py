from re import A
import sys
from time import sleep

from pyparsing import Word
from packages.jobcan.Application.jobcan_login_service import JobcanLoginService
from selenium.webdriver.support.ui import Select
from shared.Domain.Scraping.xweb_element import XWebElement
from shared.Domain.xregex import XRegex
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from shared.Domain.xstr import XStr


# ①ログイン時に当日の工数を一旦08:00で登録する
# ②週末に、入力が不正なデータ行を洗い出して抽出し、個別に手動で修正


# ①
web_browser_operator = JobcanLoginService().handle()


edit_btn = web_browser_operator.find_by_css_selector(
    css_selector=".today-record > td > div"
)

edit_btn.web_element().click()

sleep(2)
dropdown = web_browser_operator.find_by_xpath(xpath="//*[@id='select-template']/select")
select = Select(dropdown.web_element())
select.select_by_index(1)

modal_title = web_browser_operator.find_by_class_name(class_name="modal-title").first()
xregex = XRegex("(?<=\＝).+")
working_time = xregex.partial_match(XStr(modal_title.web_element().text))
sleep(2)
working_time_input = web_browser_operator.find_by_css_selector(
    "#save-form .man-hour-input"
).web_element()

working_time_input.clear()
working_time_input.send_keys(working_time)
sleep(2)
web_browser_operator.find_by_id("save").web_element().click()


# ②
trs = web_browser_operator.search_by_css_selector(css_selector="tbody tr")

target_rows = []

for tr in trs.all():

    # ['03/24木', '08:00', '08:00', '編集']のようなリスト
    row_text_list = XStr(tr.web_element().text).to_list(" ")

    total_working_time = row_text_list[1]
    total_man_hours = row_text_list[2]

    if total_working_time != "00:00" and total_working_time != total_man_hours:
        target_rows.append(row_text_list)


# total_working_time = tr.web_element().get_attribute("innerHTML")

# wait = WebDriverWait(web_browser_operator.webdriver(), 10)
# wait.until(EC.presence_of_all_elements_located)

# a = WebDriverWait(web_browser_operator.webdriver(), 10).until(
#     EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".jbc-text-reset"))
# )

print("hoge")
