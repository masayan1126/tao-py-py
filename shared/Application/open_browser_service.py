from time import sleep

from shared.Domain.xbrowser import XBrowser


class OpenBrowserService:
    def execute(self, xbrowser: XBrowser, needs_multiple_tags):

        driver = xbrowser.get_web_scraper()

        if needs_multiple_tags:
            # 新しいタブを作成する
            driver.execute_script("window.open()")

            # 新しいタブに切り替える
            driver.switch_to.window(driver.window_handles[-1])

        driver.get(xbrowser.get_url())
        driver.maximize_window()
        sleep(2)
        return driver
