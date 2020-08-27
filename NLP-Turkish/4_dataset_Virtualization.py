import pandas as pd
import numpy as np


# There is no column name in dataset so we include header=None and we detect some columns name for thats and
# we give this columns names using names=column
colnames = ["speed", "service", "flavor", "delete", "review", "restoraand_id"]  # Columns names are detected and create a list.
df = pd.read_csv("C:/Users/Demir/Desktop/Loodos/comments_with_restaurant_id.tsv", sep="\t", names=colnames, header=None)
# print(df.isnull().sum()) # look how many cell is emty at each columns
# df.drop("delete", axis = 1, inplace=True)       # There are a column which is unknown by us so it deleted.
print(df.info(), df.head(5), df.describe().T, sep="\n\n")

# # Restourantlarla ilgili yorum sayıları, ortalama puanları, standart sapmaları bilgileri yazdırılır.
# print(df.groupby("restoraand_id").count(),
#       df.groupby("restoraand_id").mean(),
#       df.groupby("restoraand_id").std())


print(df.groupby("restoraand_id").aggregate([np.median, np.std]))

print(df.isnull().sum())

# import matplotlib.pyplot as plt
# df.groupby("restoraand_id").count().plot()
# plt.show()





