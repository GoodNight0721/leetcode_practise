import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates(subset=['sell_date', 'product'])
    activities = activities.sort_values(['sell_date', 'product'])
    df1 = activities.groupby('sell_date', as_index=False)['product'].count().rename(columns={'product': 'num_sold'})
    df2 = activities.groupby('sell_date', as_index=False)['product'].agg(','.join).rename(columns={'product': 'products'})
    df = df1.merge(
        df2,
        on='sell_date',
        how='left'
    )

    return df
