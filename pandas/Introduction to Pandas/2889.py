import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    wide_df = weather.pivot(
        index='month',
        columns='city',
        values='temperature'
    )
    return wide_df