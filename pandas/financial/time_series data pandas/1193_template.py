import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.to_period('M').astype(str)
    transactions['approved'] = (transactions['state'] == 'approved').astype(int)
    transactions['approved_amount'] = transactions['amount'] * transactions['approved']
    
    transactions = (
        transactions
        .groupby(['country', 'month'], dropna=False)
        .agg(
            trans_count = ('id', 'count'),
            approved_count = ('approved', 'sum'),
            trans_total_amount = ('amount', 'sum'),
            approved_total_amount = ('approved_amount', 'sum')
        )
        .reset_index()
    )
    
    return transactions
    