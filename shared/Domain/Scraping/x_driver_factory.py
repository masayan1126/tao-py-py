from shared.Domain.Scraping.browser_judgement import BrowserJudgement
from shared.Enums.browser_type import BrowserType
from shared.factory import Factory
from shared.Domain.Scraping.xdriver import XDriver
from selenium.common.exceptions import SessionNotCreatedException


class XDriverFactory(Factory):
    def create(self, browser_type: BrowserType, is_headless=True, on_docker=False):
        try:
            judgement = BrowserJudgement(browser_type, is_headless, on_docker)
            return XDriver(judgement.judge())
        except Exception:
            raise SessionNotCreatedException
