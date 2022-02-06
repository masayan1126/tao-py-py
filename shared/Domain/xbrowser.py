class XBrowser:
    def __init__(self, browser_object, url):
        self.url = url
        self.browser_object = browser_object
        
    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url
        return self

    def get_browser_object(self):
        return self.browser_object