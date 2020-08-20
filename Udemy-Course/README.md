# Verisetinin hikayesi nedir? Nereden nasıl gelmiştir?

1. Verilen verisetinin bir yedeğini al. <br>
df = df_planets.copy()

2. Yapısal bilgilerine bakalım.<br>
  ```df.info()```

3. Objeleri Categorigal değişkenine çevir<br>
  ```df.objName = pd.Categoricial(df.ObjName)```

4. Eksik gözlem var mı?<br>
  ```df.isnull().values.any()   # True ise vardır.```<br>
  ```df.isnull().sum()   # kaç tane?```<br>
  ```df["colname"].fillna(0, inplace = True) #eksik olan değerleri 0 ile doldurur kalıcı olarak.``` 

Kategorik değişken != String. Object olarak adlandırılırlar. Bunları ayrı bir df ye almaka için:<br>
  ```kat_df = df.["colName"].select.dtypes(include = ["Object"])```
