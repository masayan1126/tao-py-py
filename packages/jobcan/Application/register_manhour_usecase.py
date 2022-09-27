from time import sleep

from selenium.webdriver.support.ui import Select
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Regex.xregex import XRegex
from selenium.webdriver.common.by import By
from shared.Domain.String.xstr import XStr
from selenium.webdriver.common.keys import Keys


class RegisterManhourUseCase:
    def handle(self, web_browser_operator: IWebBrowserOperator):
        records = web_browser_operator.search_by_css_selector(css_selector="tbody > tr")
        today_record_index = 0

        for i, record in enumerate(records.all()):
            if record.web_element().get_attribute("class") == "today-record ":
                today_record_index = i

        if today_record_index != 0:
            yestaday_record = records.all()[today_record_index - 1]

        edit_btn = yestaday_record.web_element().find_element(
            By.CSS_SELECTOR, "td > div"
        )
        edit_btn.click()

        sleep(2)
        dropdown = web_browser_operator.find_by_xpath(
            xpath="//*[@id='select-template']/select"
        )
        select = Select(dropdown.web_element())
        select.select_by_index(1)

        modal_title = web_browser_operator.find_by_class_name(
            class_name="modal-title"
        ).first()
        xregex = XRegex("(?<=\＝).+")
        working_time = xregex.partial_match(XStr(modal_title.web_element().text))
        sleep(2)
        working_time_input = web_browser_operator.find_by_css_selector(
            "#save-form .man-hour-input"
        ).web_element()

        working_time_input.clear()
        working_time_input.send_keys(working_time)
        sleep(3)
        # 一度タブキーを押さないと保存ボタンが押せない
        working_time_input.send_keys(Keys.TAB)
        web_browser_operator.find_by_id("save").click()
        sleep(3)
