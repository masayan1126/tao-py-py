from time import sleep

class OpenBrowserService:
    def execute(self,browser):
        browser.get_browser_object().get(browser.get_url())
        sleep(2)