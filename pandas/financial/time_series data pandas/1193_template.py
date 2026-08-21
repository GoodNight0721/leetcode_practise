import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['trans_date'] = transactions['trans_date'].dt.to_period('M').astype(str)
    transactions['approved'] = (transactions['state'] == 'approved').astype(int)
    transactions['approved_amount'] = transactions['amount'] * transactions['approved']
    
    transactions = (
        transactions
        .groupby(['country', 'trans_date'], dropna=False)
        .agg({
            'state': 'count',
            'approved': 'sum',
            'amount': 'sum',
            'approved_amount': 'sum'
        })
        .reset_index()
        .rename(
            columns={
                'state': 'trans_count',
                'approved': 'approved_count',
                'amount': 'trans_total_amount',
                'approved_amount': 'approved_total_amount',
                'trans_date': 'month'
            }
        )
    )
    
    return transactions
    