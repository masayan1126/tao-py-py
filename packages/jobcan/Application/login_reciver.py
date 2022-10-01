from time import sleep

from shared.Domain.String.xstr import XStr
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.Domain.Text.x_text import XText
from shared.Domain.Text.text_file_service import TextFileService


class LoginReciver:
    def __str__(self):
        pass

    def action(self, web_browser_operator: WebBrowserOperator) -> None:
        user_email = web_browser_operator.find_by_id(id_name="user_email")
        user_password = web_browser_operator.find_by_id(id_name="user_password")

        web_browser_operator.send_value(
            XWebElementList(
                [
                    user_email.set_value(self.auth_info()[0]),
                    user_password.set_value(self.auth_info()[1]),
                ]
            )
        )
        web_browser_operator.find_by_xpath(xpath="//*[@id='new_user']/input[2]").click()

        sleep(1)

        web_browser_operator.find_by_xpath(
            xpath="/html/body/div[1]/header/nav/div/div[2]/ul/li[3]/a"
        ).click()

    def auth_info(self) -> list[str]:

        return TextFileService(
            x_text=XText(
                XFileSystemPath(XStr("packages/jobcan/auth_info.txt")).to_absolute()
            )
        ).readlines(encoding="UTF-8")
