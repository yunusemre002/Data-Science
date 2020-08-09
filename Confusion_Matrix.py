from sklearn.metrics import confusion_matrix, classification_report

secim_true = ["LDP", "LDP", "VP", "VP", "LDP", "VP", "VP", "LDP", "VP", "LDP",
              "LDP", "VP", "LDP", "LDP", "VP", "LDP", "LDP", "LDP", "VP", "LDP"]

secim_pred = ["VP", "VP", "VP", "LDP", "LDP", "VP", "VP", "LDP", "VP", "VP", "LDP",
              "LDP", "LDP", "LDP", "VP", "VP", "LDP", "LDP", "LDP", "LDP"]

data = confusion_matrix(secim_true, secim_pred)
print('Confusion Matrix  :', data)
print('Report : ', classification_report(secim_true, secim_pred), sep="\n")

# ------------------------------ Virtulazation --------------------------------------
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df_cm = pd.DataFrame(data, columns=np.unique(secim_true), index=np.unique(secim_pred))
df_cm.index.name   = 'Actual'
df_cm.columns.name = 'Predicted'
plt.figure(figsize=(10, 7))
sn.set(font_scale=1.4)  # for label size
sn.heatmap(df_cm, cmap="Blues", annot=True, annot_kws={"size": 16})  # font size
plt.show()




# import numpy as np
# from sklearn.metrics import confusion_matrix, classification_report
#
# y_true = np.array(['cat', 'dog', 'pig', 'cat', 'dog', 'pig'])
# y_pred = np.array(['cat', 'pig', 'dog', 'cat', 'cat', 'dog'])
#
# print(y_true, y_pred, sep="\n")
# print('Confusion Matrix :', confusion_matrix(y_true, y_pred), sep="\n")
# print('Report           :', classification_report(y_true, y_pred), sep="\n")


