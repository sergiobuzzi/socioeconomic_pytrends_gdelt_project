# libraries
import os
import gcsfs
import pandas as pd
import random
import pytrends
from pytrends.request import TrendReq
from datetime import datetime, date, time, timedelta

#--------------------------------------
# due to how works pytrends, we will always request everything from 2019
#--------------------------------------
yesterday=(datetime.now()-timedelta(days=1)).date()
dates="2019-01-01"+" "+str(yesterday) 
print(dates)
keywords=[
    "zoom","teams","skype","hangouts","teletrabajo","videollamada","videoconferencia",
    "whatsapp", "telegram","viber", "tiktok",
    "refugiados", "inmigracion", "nacionalismo", "corrupcion", "juicio", "guerra comercial",
    "coronavirus", "pandemia", "infeccion", "medico",
    "disney","amazon", "netflix", "hbo", "rakuten", "steam",
    "cabify", "taxi","glovo", "just eat", "deliveroo", "uber eats",
    "comida a domicilio","hacer deporte", "yoga", "meditacion","cursos online"
    
]

pytrends = TrendReq(hl='ES', tz=0)
future_dataframe={}
c=1
for k in keywords:   
    
    try:
        print("Requesting ",[k])
        pytrends.build_payload([k], timeframe=dates, geo='ES', gprop='')
        future_dataframe[c]=pytrends.interest_over_time() 
        future_dataframe[c].drop(['isPartial'], axis=1,inplace=True)
        c+=1
        result = pd.concat(future_dataframe, axis=1)
    except:
        print("***","\n","Error with ",k,"or not enough trending percentaje","\n","***")

result.columns = result.columns.droplevel(0)
df1=result.unstack(level=-1)
df2=pd.DataFrame(df1)
df2.to_csv(os.getenv("PROJECT_TMP"))