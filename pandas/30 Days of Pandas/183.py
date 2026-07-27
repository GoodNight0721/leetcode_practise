import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df1 = customers
    df2 = orders

    df2 = df2.rename(
        columns={
            'customerId': 'id',
            'id': 'a'
        }
    )

    df = pd.merge(
        df1,
        df2,
        on='id',
        how='left'
    )

    output = df.loc[(df['a'].isna()), ['name']]
    output = output.rename(
        columns={
            'name': 'Customers'
        }
    )

    return output