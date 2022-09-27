from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Scraping.i_web_browser_operator import IWebBrowserOperator
from shared.Domain.Scraping.xweb_element_list import XWebElementList
from shared.Domain.String.xstr import XStr
from shared.Domain.Text.text_file_service import TextFileService
from shared.Domain.Text.x_text import XText


class LoginXserverReciver:
    def action(self, web_browser_operator: IWebBrowserOperator) -> None:
        user_email = web_browser_operator.find_by_id(id_name="memberid")
        user_password = web_browser_operator.find_by_id(id_name="user_password")

        web_browser_operator.send_value(
            XWebElementList(
                [
                    user_email.set_value(self.auth_info()[0]),
                    user_password.set_value(self.auth_info()[1]),
                ]
            )
        )

        login_btn = web_browser_operator.find_by_xpath(
            xpath="/html/body/main/div[1]/div/form/div[2]/div[1]/input[2]"
        )

        login_btn.click()

    def auth_info(self) -> tuple[str, str]:
        auth_info = TextFileService(
            XText(XFileSystemPath(XStr("packages/xserver/auth_info.txt")))
        ).readlines(encoding="UTF-8")
        email = auth_info[0]
        password = auth_info[1]

        return email, password