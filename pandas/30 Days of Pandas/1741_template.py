import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    result = employees.groupby(['emp_id', 'event_day'], as_index=False)['total_time'].sum()
    return result.rename(
        columns={
            'event_day': 'day',
        }
    )