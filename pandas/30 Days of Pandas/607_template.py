import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_id = company.loc[company['name'] == 'RED', 'com_id']

    bad_sales_ids = orders.loc[orders['com_id'].isin(red_id), 'sales_id']

    result = sales_person.loc[~sales_person['sales_id'].isin(bad_sales_ids), ['name']]

    return result