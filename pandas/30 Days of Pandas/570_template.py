import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    result = employee.groupby('managerId', as_index=False)['id'].count()
    result = result.loc[result['id'] >= 5]
    result = employee.loc[employee['id'].isin(result['managerId']), ['name']]

    return result