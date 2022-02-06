
class Issue:

    def __init__(self, title, label):
        self.title = title
        self.label = label

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title
        return self

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label
        return self
    
    # TODO:body