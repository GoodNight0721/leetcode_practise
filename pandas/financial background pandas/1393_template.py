import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks.loc[stocks['operation'] == 'Buy', 'price'] = -stocks['price']
    output = stocks.groupby('stock_name')['price'].sum().reset_index().rename(columns={'price': 'capital_gain_loss'})
    return output