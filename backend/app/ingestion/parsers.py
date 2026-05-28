import pandas as pd


def parse_csv(file_path):

    dataframe = pd.read_csv(
        file_path
    )

    return dataframe.to_dict(
        orient="records"
    )