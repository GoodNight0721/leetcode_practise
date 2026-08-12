import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df1 = daily_sales.groupby(['date_id', 'make_name'], as_index=False)['lead_id'].nunique().rename(columns={'lead_id': 'unique_leads'})
    df2 = daily_sales.groupby(['date_id', 'make_name'], as_index=False)['partner_id'].nunique().rename(columns={'partner_id': 'unique_partners'})
    df = df1.merge(
        df2,
        on=['date_id', 'make_name'],
        how='left'
    )

    return df
