from shared.Domain.Scraping.browser_judgement import BrowserJudgement
from shared.Enums.browser_type import BrowserType
from shared.i_factory import IFactory
from shared.Domain.Scraping.xdriver import XDriver
from shared.Domain.Scraping.xdriver import XDriver
from shared.Enums.browser_type import BrowserType


class XDriverFactory(IFactory):
    def create(self, browser_type: BrowserType, is_headless=True):
        judgement = BrowserJudgement(browser_type, is_headless)
        return XDriver(judgement.judge())
