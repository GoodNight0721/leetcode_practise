import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(
        method='dense',
        ascending=False
    )

    scores = scores.sort_values('rank')

    return scores[['score', 'rank']]