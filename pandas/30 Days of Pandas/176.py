import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee
    salary = df['salary'].drop_duplicates().sort_values()
    if len(salary) < 2:
        result = None
    else:
        result = salary.iloc[-2]
    return pd.DataFrame({
        'SecondHighestSalary': [result]
    })