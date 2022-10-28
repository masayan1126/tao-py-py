from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.Domain.String.xstr import XStr
from shared.Domain.DataFile.TextFile.text_file_operator_factory import (
    TextFileOperatorFactory,
)


class LoginXserverReciver:
    def __init__(self, web_browser_operator: WebBrowserOperator):
        self.web_browser_operator = web_browser_operator

    def action(self) -> None:
        user_email = self.web_browser_operator.find_by_id(id_name="memberid")
        user_password = self.web_browser_operator.find_by_id(id_name="user_password")

        self.web_browser_operator.send_value(
            XWebElementList(
                [
                    user_email.set_value(self._auth_info()[0]),
                    user_password.set_value(self._auth_info()[1]),
                ]
            )
        )

        login_btn = self.web_browser_operator.find_by_xpath(
            xpath="/html/body/main/div[1]/div/form/div[2]/div[1]/input[2]"
        )

        login_btn.click()

    def _auth_info(self) -> tuple[str, str]:
        text_file_operator = TextFileOperatorFactory().create(
            XFileSystemPath(XStr("packages/xserver/auth_info.txt"))
        )

        auth_info = text_file_operator.readlines(encoding="UTF-8")
        email = auth_info[0]
        password = auth_info[1]

        return email, password
