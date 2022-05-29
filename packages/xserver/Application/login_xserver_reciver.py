from time import sleep
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.Domain.String.xstr import XStr
from shared.Domain.Text.text_file_service import TextFileService
from shared.Domain.Text.x_text import XText
from shared.i_command import ICommand


class LoginXserverReciver(ICommand):
    def __str__(self):
        pass

    def action(self, i_web_browser_operator: IWebBrowserOperator) -> None:
        user_email = i_web_browser_operator.find_by_id(id_name="memberid")
        user_password = i_web_browser_operator.find_by_id(id_name="user_password")

        i_web_browser_operator.send_value(
            XWebElementList(
                [
                    user_email.set_value(self.login_info()[0]),
                    user_password.set_value(self.login_info()[1]),
                ]
            )
        )
        i_web_browser_operator.find_by_xpath(
            xpath="/html/body/main/div[1]/div/form/div[2]/div[1]/input[2]"
        ).web_element().click()

        sleep(1)

    def login_info(self) -> tuple[str, str]:
        login_info = TextFileService(
            XText(XFileSystemPath(XStr("packages/xserver/password.txt")))
        ).readlines(encoding="UTF-8")
        email = login_info[0]
        password = login_info[1]

        return email, password
