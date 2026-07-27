import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views.loc[views['author_id'] == views['viewer_id'], ['viewer_id']].rename(columns={'viewer_id': 'id'})
    df = df.drop_duplicates()
    df = df.sort_values('id')
    return df
