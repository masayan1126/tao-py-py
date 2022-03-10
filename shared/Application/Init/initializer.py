import io, sys
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from webdriver_manager.chrome import ChromeDriverManager
from shared.Domain.xdriver import XDriver
from shared.Enums.browser_type import BrowserType



class Initializer:
    def webBrowserOption(self, browser_type:BrowserType, is_headless=True) -> XDriver:

        match browser_type:
            case browser_type.CHROME:

                # TODO: このオプションを生成するクラスを別途作成する(WebDriverOption)
                chrome_options = webdriver.ChromeOptions()
                
                # Chrome は自動テストソフトウェアによって制御されています。の表示とログ出力を非表示に
                chrome_options.add_experimental_option(
                    "excludeSwitches", ["enable-automation", "enable-logging"]
                )

                # 処理完了後もブラウザが起動している状態を保持する
                chrome_options.add_experimental_option(
                    "detach", True
                )

                if is_headless:
                    chrome_options.add_argument("--headless")

                chrome_service = fs.Service(executable_path=ChromeDriverManager().install())
                return XDriver(chrome_service, chrome_options, "Chrome")
            case browser_type.FIREFOX:
                # TODO:firefox
                pass
            case _:
                pass

    def ioOption(self) -> None:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")