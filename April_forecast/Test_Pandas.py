import requests
import pandas as pd
from requests import head


def wszystkie_kraje():
    url = "https://restcountries.com/v3.1/all?fields=name,flags,population,subregion,independent"
    odpowiedz = requests.get(url)
    dane = odpowiedz.json()

    kraje = []
    for x in dane:
        nowy = {
            "nazwa": x.get("name").get("common"),
            "oficjalna_nazwa": x.get("name").get("official"),
            "flaga": x.get("flags").get("png"),
            "populacja": x.get("population"),
            "niepodleglosc": x.get("independent"),
            "region": x.get("subregion"),

        }
        kraje.append(nowy)

    return kraje

lista_krajów = wszystkie_kraje()

df = pd.DataFrame(lista_krajów)

top_5_europa = df[df['region'].str.contains('Europe', na=False)].sort_values(by='populacja', ascending=False).head(5)
# result = wszystkie_kraje()
#
# df = pd.DataFrame(result)
# df.to_excel("kraje.xlsx", index=False)

df = pd.read_excel("kraje.xlsx")

a = df.head(3)
b = df.tail(3)

# df.info()

c = df.describe()

d = list(df.columns)

# pd.set_option("display.max_columns", None)
# pd.set_option('display.max_rows', None)
# SORTOWANIE
e = df.sort_values("populacja" == "Europe").ascending=False,head(5)
# print(e[["nazwa","populacja"]])
f = df.sort_values("nazwa")
# print(f)

# FILTROWANIE
g = df[ (df["populacja"] < 100_000_000) & (df["niepodleglosc"] == False)]
h = df[ df["region"] == "Eastern Asia" ]
i = df[ (df["region"] == "Europe")]


print(top_5_europa[['nazwa', 'populacja']])

