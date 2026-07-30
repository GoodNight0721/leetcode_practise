import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee

    salary = df['salary'].drop_duplicates().sort_values()
    if N <= 0 or len(salary) < N:
        result =  None
    else:
        result = salary.iloc[-N]

    return pd.DataFrame({
        f'getNthHighestSalary({N})' : [result]
    })