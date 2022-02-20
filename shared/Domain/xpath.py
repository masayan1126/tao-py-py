from urllib.parse import urlparse
from urllib.parse import urljoin


class XPath:
    def __init__(self, path: str):
        self.path = path

    def get_path(self):
        return self.path
