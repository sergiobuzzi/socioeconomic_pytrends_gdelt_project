import pandas as pd

df2=pd.read_csv("PROJECT_TMP")

keywords_new=pd.DataFrame()
keywords_new["date"]=df2["date"]
keywords_new["trend_index"]=df2["0"]
keywords_new["keyword"]=df2['Unnamed: 0']

if keywords_new['trend_index'].isnull().values.any()==True:
    keywords_new["trend_index"]=keywords_new["trend_index"].fillna(0)

keywords_final=pd.DataFrame(keywords_new)
keywords_final.to_csv("PROJECT_TMP")