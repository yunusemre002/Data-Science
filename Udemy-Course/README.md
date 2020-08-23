# Verisetinin hikayesi nedir? Nereden nasıl gelmiştir?

1. Verilen verisetinin bir yedeğini al. <br>
df = df_planets.copy()

2. Yapısal bilgilerine bakalım.<br>
  ```df.info()```<br>
  ```df.describe().T```
  

3. Objeleri Categorigal değişkenine çevir<br>
  ```df.objName = pd.Categoricial(df.ObjName)```<br>
  a. Bunu sıralaı olarak yapacaksan<br>
    Önce sıralamayı belirten bir liste yap:<br>
    ```cut_kategoriler = ["Fair","Good","Very Good","Premium","Ideal"]```<br>
    Sonra dönüşümü o listeye göre yap<br>
    ```df.cut = df.cut.astype(CategoricalDtype(categories = cut_kategoriler, ordered = True))```

4. Eksik gözlem var mı?<br>
  ```df.isnull().values.any()   # True ise vardır.```<br>
  ```df.isnull().sum()   # kaç tane?```<br>
  ```df["colname"].fillna(0, inplace = True) #eksik olan değerleri 0 ile doldurur kalıcı olarak.``` 

Kategorik değişken != String. Object olarak adlandırılırlar. Bunları ayrı bir df ye almaka için:<br>
  ```kat_df = df.["colName"].select.dtypes(include = ["Object"])```

Sayıların unic değerlerle vermek için: <br>
 ```kat_df["colName"].value_counts()```

Görselleştirmek için:<br>
 ```kat_df["colName"].value_counts().plot.barh()```
 
 # Sütun grafikler Kategorik değişkenleri görsellştirmek için kullanılır. (Barplot)

Basit bir renkli grafik oluşturmak. Basit x ve y yi ver hangi df kullanılacak onu ver ve tamam.<br>
```sns.barplot(x = "cut", y = df.cut.index, data= df);```

