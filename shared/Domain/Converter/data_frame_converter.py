from pandas import DataFrame


class DataFrameConverter:
    def to_dictionary(df: DataFrame) -> dict:
        return df.to_dict("index").values()

    def to_list(df: DataFrame) -> list:
        return list(df.to_dict("index").values())
