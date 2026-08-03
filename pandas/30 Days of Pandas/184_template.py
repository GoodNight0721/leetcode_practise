import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salary = employee.groupby('departmentId')['salary'].transform('max')
    top_employee = employee.loc[
        employee['salary'] == max_salary
    ]

    top_employee = top_employee.rename(
        columns={
            'name': 'Employee'
        }
    )

    result = top_employee.merge(
        department,
        left_on='departmentId',
        right_on='id',
        how='left'
    )

    result = result.rename(
        columns={
            'name': 'Department',
            'salary': 'Salary'
        }
    )

    return result[['Department', 'Employee', 'Salary']]