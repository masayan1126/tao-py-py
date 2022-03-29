from typing import Dict
from pandas import DataFrame


class DataFrameConverter:
    def to_dictionary(df: DataFrame) -> Dict:
        # print(df.empty)
        return df.to_dict("index").values()
