from selenium import webdriver

class XDriver:
    def __init__(self, service, options, type):
        self.service = service
        self.options = options
        self.type = type
        
    def get_driver(self):
        if self.type=="Chrome":
            return webdriver.Chrome(service=self.service,options=self.options)