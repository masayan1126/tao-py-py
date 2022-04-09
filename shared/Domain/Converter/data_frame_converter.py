from typing import Dict, List
from pandas import DataFrame


class DataFrameConverter:
    def to_dictionary(df: DataFrame) -> Dict:
        # print(df.empty)
        return df.to_dict("index").values()

    def to_list(df: DataFrame) -> List:
        return list(df.to_dict("index").values())
