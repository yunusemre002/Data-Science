from sklearn.feature_extraction import DictVectorizer
from collections import Counter

File_1 = ('a', 'b', 'c', 'd', 'a')
File_2 = ('aa', 'a')

# for f in (File_1, File_2):
#     print(f)
#     print(Counter(f))

# discover corpus and vectorize file word frequencies in a single pass
v = DictVectorizer()
X = v.fit_transform(Counter(f) for f in (File_1, File_2))

print(X)
print(X.A)  # For looks list
