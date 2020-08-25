import pandas as pd
from zemberek import TurkishSentenceNormalizer, TurkishMorphology

# İMPORT DATASET
# There is no column name in dataset so we include header=None and we detect some columns name for thats and
# we give this columns names using names=column

# Columns names are detected and create a list.
colnames = ["speed", "service", "flavor", "delete", "review", "restoraand_id"]
df = pd.read_csv("C:/Users/Demir/Desktop/Loodos/comments_with_restaurant_id.tsv", sep="\t", names=colnames, header=None)
df.drop("delete", axis = 1, inplace=True)                     # There are a column which is unknown by us so it deleted.
# print(df.info(), df.head(5), df.describe().T, sep="\n\n")

df = df.sample(frac = 0.0001, replace = False, random_state=17) # Take just a few of all reviews
print(df.shape)


# SENTENCE NORMALIZATION
morphology = TurkishMorphology.create_with_defaults()
normalizer = TurkishSentenceNormalizer(morphology)

for i in df["review"]:
    print(i)
    print(normalizer.normalize(i), "\n")
