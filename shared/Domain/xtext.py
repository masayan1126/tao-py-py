class XText:
    def __init__(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        return self
