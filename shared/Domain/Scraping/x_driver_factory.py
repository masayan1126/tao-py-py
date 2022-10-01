from shared.Domain.Log.x_logger import XLogger
from shared.Domain.Scraping.browser_judgement import BrowserJudgement
from shared.Enums.browser_type import BrowserType
from shared.Core.factory import Factory
from shared.Domain.Scraping.xdriver import XDriver



class XDriverFactory(Factory):
    # 本来のfactoryパターンの使い方
    def create(self, browser_type: BrowserType, is_headless=True, on_docker=False):
        judgement = BrowserJudgement(browser_type, is_headless, on_docker)

        return XDriver(judgement.judge())
