from shared.Domain.Scraping.browser_type import BrowserType
from shared.Core.judgement import Judgement
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from webdriver_manager.chrome import ChromeDriverManager


class BrowserDriverTypeJudgement(Judgement):
    def __init__(self, browser_type, is_headless):
        self.browser_type = browser_type
        self.is_headless = is_headless

    def judge(self):
        # 本番のpythonがanacondaの関係で3.9.4のためmatch～case文ではなくif文を使用する
        if self.browser_type == BrowserType.CHROME:
            chrome_service = fs.Service(executable_path=ChromeDriverManager().install())
            return webdriver.Chrome(
                service=chrome_service, options=self.chrome_options()
            )
        # TODO:firefox
        else:
            pass

    def chrome_options(self):
        chrome_options = webdriver.ChromeOptions()

        # Chrome は自動テストソフトウェアによって制御されています。の表示とログ出力を非表示に
        chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-automation", "enable-logging"]
        )

        # 処理完了後もブラウザが起動している状態を保持する
        chrome_options.add_experimental_option("detach", True)

        if self.is_headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")

        return chrome_options
