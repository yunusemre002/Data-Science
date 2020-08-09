import pandas as pd
from nltk import re

df = pd.read_csv("covid19_tweets.csv", usecols=['text'])
df = df.sample(frac = 0.001, replace = False, random_state=42)      # Take %0.5 of total reviews
print(df.describe())

for tweet in df['text']:
    print("\n", tweet)
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet)  # Remove links
    tweet = re.sub('((@[^\s]+)|(#[^\s]+))', '', tweet)              # Remove Mension and Hashtag
    tweet = re.sub('[\s]+', ' ', tweet)                             # Remove additional white spaces
    # tweet = tweet.strip('\'"')     # trim
    print(tweet)