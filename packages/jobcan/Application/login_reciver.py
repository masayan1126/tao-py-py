import os
from time import sleep
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.i_command import ICommand


class LoginReciver(ICommand):
    def __str__(self):
        pass

    def action(self, i_web_browser_operator: IWebBrowserOperator) -> None:
        user_email = i_web_browser_operator.find_by_id(id_name="user_email")
        user_password = i_web_browser_operator.find_by_id(id_name="user_password")

        i_web_browser_operator.send_value(
            XWebElementList(
                [
                    user_email.set_value(os.environ.get("AIVICK_EMAIL")),
                    user_password.set_value(os.environ.get("JOBCAN_PASSWORD")),
                ]
            )
        )
        i_web_browser_operator.find_by_xpath(
            xpath="//*[@id='new_user']/input[2]"
        ).web_element().click()

        sleep(1)

        i_web_browser_operator.find_by_xpath(
            xpath="/html/body/div[1]/header/nav/div/div[2]/ul/li[3]/a"
        ).web_element().click()
