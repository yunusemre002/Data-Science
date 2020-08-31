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


# SENTENCE NORMALIZATION
morphology = TurkishMorphology.create_with_defaults()
normalizer = TurkishSentenceNormalizer(morphology)

# # Option 1. --------------------For select random 150 reviews--------------
# df = df.sample(frac = 0.0001, replace = False, random_state=17) # Take just a few of all reviews
# print(df.shape)
# for i in df["review"]:
#     print(i)
#     print(normalizer.normalize(i), "\n")

# # Option 2. -------------------For select first 10 reviews:----------------
# for i in df.review[:10]:                      # Slider, select first 10 row from review in df
#     print(i)
#     print(normalizer.normalize(i), "\n")


# Option 3. -------------------- For write to txt--------------
# df = df.sample(frac = 0.0001, replace = False, random_state=17) # Take just a few of all reviews
outF = open("CommentNormalized.txt", "w+", encoding="utf-8")


import time
import logging
logger = logging.getLogger(__name__)
start = time.time()



for index, i in enumerate(df["review"]):
    i_normalized = normalizer.normalize(i)
    print("{}\n{} {}\n".format(i, i_normalized, index))
    outF.write("%s \n%s\n\n" % (i, i_normalized))


logger.info(f"Normalization instance created in: {time.time() - start} s")



outF.close()