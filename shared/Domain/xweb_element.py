from shared.Domain.i_xweb_element import IXWebElement


class XWebElement(IXWebElement):
    def __init__(self, key, element, value):
        self.key = key
        self.element = element
        self.value = value

    def get_key(self):
        return self.key

    def get_element(self):
        return self.element

    def get_value(self):
        return self.value
