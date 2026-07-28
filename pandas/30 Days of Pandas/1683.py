import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets
    return df.loc[df['content'].str.len() > 15, ['tweet_id']]