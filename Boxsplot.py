# Sütun grafikler kategorik değişkenleri görselleştirirken
# Boxplot grafikler ise genelde sayısal verileri görselleştirmek için kullanılır.
#

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
df = tips.copy()
# print(df.head())
print(df.describe().T)
print()
print(df["sex"].value_counts())

# sns.boxplot( x = df["total_bill"])
#
# # Hangi günlerde daha faza apra kazanıyoruz.
# sns.boxplot( x = "day", y = "total_bill", data=df)

# sns.boxplot( x = "day", y = "total_bill", hue="sex", data=df)

# sns.scatterplot(x = "total_bill", y = "tip", data = df);

sns.scatterplot(x = "total_bill", y = "tip", hue= "size", size = "size", data = df);
plt.show()