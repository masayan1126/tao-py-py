from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.String.xstr import XStr
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.Domain.DataFile.TextFile.text_file_operator_factory import (
    TextFileOperatorFactory,
)


class LoginJobcanReciver:
    def __init__(self, web_browser_operator: WebBrowserOperator):
        self.web_browser_operator = web_browser_operator

    def action(self) -> None:
        user_email_input = self.web_browser_operator.find_by_id(id_name="user_email")
        user_password_input = self.web_browser_operator.find_by_id(
            id_name="user_password"
        )

        self.web_browser_operator.send_value(
            XWebElementList(
                [
                    user_email_input.set_value(self._auth_info()[0]),
                    user_password_input.set_value(self._auth_info()[1]),
                ]
            )
        )

        login_btn = self.web_browser_operator.find_by_xpath(
            xpath="//*[@id='new_user']/input[2]"
        )

        login_btn.click()

    def _auth_info(self) -> list[str]:
        text_file_operator = TextFileOperatorFactory().create(
            XFileSystemPath(XStr("packages/jobcan/auth_info.txt")).to_absolute()
        )

        return text_file_operator.readlines(encoding="UTF-8")
