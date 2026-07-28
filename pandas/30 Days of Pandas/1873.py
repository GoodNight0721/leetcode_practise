import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees
    df['bonus'] = df.loc[(df['employee_id'] % 2 == 1) & (~df['name'].str.startswith('M')), ['salary']]
    df = df.loc[:, ['employee_id', 'bonus']].fillna(0)
    df = df.sort_values('employee_id')
    return df