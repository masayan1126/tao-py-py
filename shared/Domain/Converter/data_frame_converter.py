from pandas import DataFrame


class DataFrameConverter:
    def to_dictionary(df: DataFrame):
        return df.to_dict("index").values()
