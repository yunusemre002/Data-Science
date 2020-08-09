import pandas as pd

# df = pd.read_csv("covid19_tweets.csv", usecols=['text'] )      # Read data. Important!

df = pd.read_csv("Reddit_Data.csv", usecols=['clean_comment'])      # Read data. Important!
df = df.rename(columns={'clean_comment': 'text'})

print(df.describe())
# df = df.sample(frac = 0.005, replace = False, random_state=42) # Take %0.5 of 568.454 reviews
print(df.count(), df.describe(), sep="\n")

# ------------------------------------------------PREPROCCESSİNG---------------------------------------------------
from nltk import re

def clean_text(text):
    text = str(text)
    text = text.lower()  # lower text
    # # --------------- For Twetter ----------------------------------
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', text)
    text = re.sub('((@[^\s]+)|(#[^\s]+))', '', text)
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = re.sub('[\s]+', ' ', text)      # Remove +++  space
    return (text)


# ------------------------------------------------SENTİMENT ANALYSES---------------------------------------------------
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    print(sentence)
    sid_obj = SentimentIntensityAnalyzer()  # Create a SentimentIntensityAnalyzer object.
    score = sid_obj.polarity_scores(sentence)
    # NewValue = (((score["compound"] - (-1.0)) * (5.0 - 1.0)) / (1.0 - (-1.0))) + 1.0
    # print("Overall sentiment dictionary is : ", score, " Predict :", NewValue, end="")
    print("SA :", score, "\n")
    return score["compound"]


if __name__ == "__main__":
    negative = positive = notr = 0

    for t in range(len(df)):
        i = str(df['text'].values[t])
        compound = sentiment_scores(clean_text(i))  # sentiment_scores(clean_text(i))

        if compound > 0:           # Positive
            positive += 1
        elif compound == 0:        # Nötr
            notr += 1
        else:                   # Negative  (sonuc < 0)
            negative += 1

    print(positive,notr,negative)
    scoreDict = { 'positive':positive,
                  'notr': notr,
                  'negative':negative
                }

    import matplotlib.pyplot as plt

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = scoreDict.keys()
    sizes = scoreDict.values()
    explode = (0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.set_title("Sentiment Analysis of Tweets")
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


    # ----------- Other Graph --------------
    plt.title('Sentiment Analysis')
    plt.figure(figsize=(8, 4))
    plt.bar(*zip(*scoreDict.items()))

    plt.show()