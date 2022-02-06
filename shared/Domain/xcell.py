from pandas import DataFrame


class XCell:
    def __init__(self, df: DataFrame, index, column):
        self.df = df
        self.index = index
        self.column = column

    def set_value(self):
        self.value = self.df.iat[self.index, self.column]
        return self

    def get_value(self):
        return self.df.iat[self.index, self.column]
