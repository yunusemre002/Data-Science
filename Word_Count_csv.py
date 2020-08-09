import re, nltk, pandas
from operator import itemgetter
from collections import OrderedDict
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
wordnet_lemmatizer = WordNetLemmatizer()

df = pandas.read_csv("Reddit_Data.csv", usecols=['clean_comment'])
df = df.rename(columns={'clean_comment': 'text'})

# print(df.describe())
# df = df.sample(frac=0.01, replace=False, random_state=42) # Take %0.5 of 568.454 reviews
# print(df.count(), df.describe(), sep="\n")


# -------------------------- Clean Dataset and Create a List of (str)all Reviews/Tweets ------------------------------------
listOfReviews = []
for i in df['text']:
    i = str(i)
    letters = re.sub('[^a-zA-Z]', ' ', i)  # Remove out of word
    tokens = nltk.word_tokenize(letters)
    lowercase = [l.lower() for l in tokens]
    filtered_result = list(filter(lambda l: l not in stop_words, lowercase))
    lemmas = [wordnet_lemmatizer.lemmatize(t) for t in filtered_result]
    listOfReviews.append(' '.join(lemmas))  # Add and of list that str.

    # print(listOfReviews)
# ['family mormon never tried explain still stare puzzled time time like kind strange creature nonetheless come
# admire patience calmness equanimity acceptance compassion developed thing buddhism teach', 'zelalem amazing', 'impressed
# gnabry movement linking seems like intelligent addition technically gifted', 'giroud fun ball mozart',
# 'zealalem make arsenal beyond amazed composure vision ball incredible reminds pirlo', ...]

#-----------------------------------------Kelime Sayaci------------------------------------------------------------

# def convert(lst):
#     return ([i for item in lst for i in item.split()])
# say = convert(listOfReviews)

say = [i for item in listOfReviews for i in item.split()]  # convert list of str to list of word (Think, like tokenize)
# 'right', 'currently', 'running', 'hd', 'magni', 'modi', 'combo', 'worth', 'upgrading', 'schiit', 'line', ...

# Look are there any word like this. İf there are add +1 else create new word whic count is 1
wordcount = {}
for word in say:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

# Wordcount is a dict which has a word (key) and word count (value)  # print(wordcount)
# We sort it by value and reverse: so big value is fist elemnet of sorted_x
sorted_x = OrderedDict(sorted(wordcount.items(), key=itemgetter(1), reverse=True))
print(sorted_x)

for key in sorted_x.keys():
    if sorted_x[key] > 1000:
        print("{} : {}".format(key, sorted_x[key]))



