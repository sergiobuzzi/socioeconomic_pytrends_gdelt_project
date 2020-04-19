# processes
import runpy
import os
from os import listdir
from os.path import isfile, join
# libraries
import gcsfs
import pandas as pd
import random
import pytrends
from pytrends.request import TrendReq
from datetime import datetime, date, time, timedelta

def main (data,context):

    #--------------------------------------
    # due to how works pytrends, we will always request everything from 2019
    #--------------------------------------
    yesterday=(datetime.now()-timedelta(days=1)).date()
    dates="2019-01-01"+" "+str(yesterday) 
    print(dates)
    keywords=[
        "zoom","teams","skype","hangouts",
        "whatsapp", "telegram","viber", "tiktok",
        "refugiados", "inmigracion", "nacionalismo", "corrupcion", "juicio", "guerra comercial",
        "coronavirus", "pandemia", "infeccion", "medico",
        "amazon", "netflix", "hbo", "rakuten", "team","cabify", "taxi", "glovo", "just eat", "deliveroo", "uber eats",
        "comida a domicilio", "hacer deporte", "yoga", "meditacion",
        "teletrabajo","videollamada","videoconferencia","cursos online"
    ]

    def tracking_in_time_keywords(kw_list):

        pytrends = TrendReq(hl='ES', tz=0)
        future_dataframe={}
        c=1
        for k in kw_list:   
            
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
        return result

    df_keywords=tracking_in_time_keywords(keywords)
    df_keywords.to_csv("../tmp/data_pytrends.csv")

    processes= ("upload_gcs.py","remove_files.py")

    for p in processes:
        exec(open(p).read())

if __name__ == "__main__":
  
    main('data','context')
 