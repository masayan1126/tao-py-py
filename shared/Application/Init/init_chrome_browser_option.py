from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from webdriver_manager.chrome import ChromeDriverManager
from shared.Domain.xdriver import XDriver
from shared.Enums.browser_type import BrowserType


class InitChromeBrowserOption:
    def execute(self, browser_type:BrowserType, is_headless=True) -> XDriver:

        match browser_type:
            case browser_type.CHROME:
                chrome_options = webdriver.ChromeOptions()
                # Chrome は自動テストソフトウェアによって制御されています。の表示とログ出力を非表示に
                chrome_options.add_experimental_option(
                    "excludeSwitches", ["enable-automation", "enable-logging"]
                )
                chrome_options.add_experimental_option(
                    "detach", True
                )  # 処理完了後もブラウザが起動している状態を保持する

                if is_headless:
                    chrome_options.add_argument("--headless")

                chrome_service = fs.Service(executable_path=ChromeDriverManager().install())
                return XDriver(chrome_service, chrome_options, "Chrome")
            case browser_type.FIREFOX:
                # TODO:firefox
                pass
            case _:
                pass