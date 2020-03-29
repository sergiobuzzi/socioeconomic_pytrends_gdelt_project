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
    ["empleo","desempleo","hipoteca","credito"],19,
    ["erte","ere"],19,
    ["centro de salud","hospital","coronavirus","ets","gripe"],45,
    ["corrupcion","juicio","politica"],19
    ]
for i in range(len(kw_list)):
    if i%2==0:
        secs=int(random.randrange(10, 50))
        print("Sleep {} seconds between requesting ".format(secs),str(kw_list[i]))
        timer.sleep(secs)
        print("Done")
        pytrends.build_payload(kw_list[i], cat=kw_list[i+1],timeframe='today 5-y', geo='ES', gprop='')
        interest_over_time_df = pytrends.interest_over_time() 
        #plotting_keywords(interest_over_time_df,kw_list[i])
        


