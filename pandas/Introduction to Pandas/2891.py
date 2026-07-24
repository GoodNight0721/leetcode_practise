import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals.sort_values('weight', ascending=False).loc[animals['weight'] > 100, ['name']]
    return df