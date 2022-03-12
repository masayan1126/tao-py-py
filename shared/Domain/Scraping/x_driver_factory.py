from types import MethodType
from shared.Enums.browser_type import BrowserType
from shared.i_factory import IFactory
from shared.Domain.Scraping.xdriver import XDriver
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from webdriver_manager.chrome import ChromeDriverManager
from shared.Domain.Scraping.xdriver import XDriver
from shared.Enums.browser_type import BrowserType


class XDriverFactory(IFactory):
    def create(self, browser_type:BrowserType, is_headless=True):
        return XDriver(self._closure(browser_type, is_headless))

    # Loan Pattern
    def _closure(self,browser_type:BrowserType, is_headless):
        def build_webdriver():
            match browser_type:
                case browser_type.CHROME:
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
                    return webdriver.Chrome(service=chrome_service, options=chrome_options)
                # TODO:firefox 
                case browser_type.FIREFOX:
                    pass
        return build_webdriver
