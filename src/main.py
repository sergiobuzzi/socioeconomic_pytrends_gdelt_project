# Libraries
import random
import pytrends
from pytrends.request import TrendReq
import pandas as pd
import time as timer 
import datetime
from datetime import datetime, date, time

# Plotting 
import matplotlib.pyplot as plt
from personal_functions import plotting_keywords
# # Security
# from google.colab import files
# from oauth2client.service_account import ServiceAccountCredentials
# from google.colab import auth
# # Saving in Google Drive
# from google.colab import  drive
# drive.mount('/drive')
# # authenticate
# auth.authenticate_user()
# gc = gspread.authorize(GC.get_application_default())
# -----------------------------------------------

# I have already installed the libraries of google cloud storage, google auth and stuff
#       https://anaconda.org/conda-forge/google-cloud-storage
# nice example of gcs
#       https://stackoverflow.com/questions/36314797/write-a-pandas-dataframe-to-google-cloud-storage-or-bigquery
# pytrends
#       https://pypi.org/project/pytrends/

# ------------------------------------------------
#this works
pytrends = TrendReq(hl='ES', tz=0)
kw_list = [
    ["empleo","paro","hipoteca","credito"],19,
    ["erte","ere","seguridad social"],19,
    ["centro de salud","hospital","coronavirus","ets","gripe"],45,
    ["corrupcion","juicio","politica"],19
    ]

#--------------------------------------
# date automation
#--------------------------------------
# yesterday=(datetime.now()-timedelta(days=1)).date()
# week_ago=(datetime.now()-timedelta(days=8)).date()
# dates=str(week_ago) + " " + str(yesterday)
dates="today 5-y"
#--------------------------------------
# the function
#--------------------------------------
def tracking_in_time_keywords(kw_list):
    pytrends = TrendReq(hl='ES', tz=0)
    future_dataframe={}
    c=1
    for i in range(len(kw_list)):
        if i%2==0:
          
            try:
                pytrends.build_payload(kw_list[i], cat=kw_list[i+1],timeframe=dates, geo='ES', gprop='')
                #interest_over_time_df = pytrends.interest_over_time() 
                future_dataframe[c]=pytrends.interest_over_time() 
                future_dataframe[c].drop(['isPartial'], axis=1,inplace=True)
                c+=1
                result = pd.concat(future_dataframe, axis=1)

                secs=int(random.randrange(10, 50))
                print("Sleeping {} seconds before requesting ".format(secs),str(kw_list[i]))
                timer.sleep(secs)
                print("Done")

            except:
                print("***","\n","Error with ",kw_list[i],"or not enough trending percentaje","\n","***")
    #result.head()
    df1=result.unstack(level=-1)
    df2=pd.DataFrame(df1)


    
    return df2

raw=tracking_in_time_keywords(kw_list)

keywords_new=pd.DataFrame()
keywords_new["date"]=raw["date"]
keywords_new["trend_index"]=raw["0"]
keywords_new["keyword"]=raw['Unnamed: 1']

if keywords_new['trend_index'].isnull().values.any()==True:
    keywords_new["trend_index"]=keywords_new["trend_index"].fillna(0)
        
# if exisist in GCS => concat axis false etc etc
# elif upload this


