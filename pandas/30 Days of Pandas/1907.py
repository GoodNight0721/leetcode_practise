import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = 0
    average = 0
    high = 0
    for i in accounts['income']:
        if i < 20000:
            low += 1
        elif i > 50000:
            high += 1
        else:
            average += 1
    
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low, average, high]
    })