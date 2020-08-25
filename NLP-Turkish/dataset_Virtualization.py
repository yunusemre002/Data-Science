import pandas as pd
import numpy as np


# There is no column name in dataset so we include header=None and we detect some columns name for thats and
# we give this columns names using names=column
colnames = ["speed", "service", "flavor", "delete", "review", "restoraand_id"]  # Columns names are detected and create a list.
df = pd.read_csv("C:/Users/Demir/Desktop/Loodos/comments_with_restaurant_id.tsv", sep="\t", names=colnames, header=None)
df.drop("delete", axis = 1, inplace=True)       # There are a column which is unknown by us so it deleted.
print(df.info(), df.head(5), df.describe().T, sep="\n\n")

# # Restourantlarla ilgili yorum sayıları, ortalama puanları, standart sapmaları bilgileri yazdırılır.
# print(df.groupby("restoraand_id").count(),
#       df.groupby("restoraand_id").mean(),
#       df.groupby("restoraand_id").std())


print(df.groupby("restoraand_id").aggregate([count, np.median, np.std]))

# import matplotlib.pyplot as plt
# df.groupby("restoraand_id").count().plot()
# plt.show()





# # ZEMBEREK PREPROCESSİNG İŞLEMLERİ ÇALIŞIYOR AMA DAHA KÖTÜ YAPIYOR SANKİ
# df_100 = df.loc[0:20, "review"] # Take just 50 review from dataset.
# # print(df_100.head(5))
#
# # SENTENCE NORMALIZATION
# from zemberek import TurkishSentenceNormalizer, TurkishMorphology
#
# morphology = TurkishMorphology.create_with_defaults()
# normalizer = TurkishSentenceNormalizer(morphology)
#
# for i in df_100:
#     print(i)
#     print(normalizer.normalize(i), "\n")

