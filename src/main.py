# Libraries
import pytrends
from pytrends.request import TrendReq
import pandas as pd
import time
import datetime
from datetime import datetime, date, time
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

TrendReq(hl='es-ES', tz=360, timeout=(10,25), proxies=['https://34.203.233.13:80','https://35.201.123.31:880'], retries=2, backoff_factor=0.1)

pytrend = TrendReq()
pytrend.build_payload(
    kw_list=["empleo","desempleo","crisis","corrupcion","centro de salud", "hospital"], 
    timeframe='today 1-m', 
    geo = 'ES')

#to get interest over time score, you'll need pytrend.interest_over_time() function.
#For more functions, check this: https://github.com/GeneralMills/pytrends
interest_over_time_df = pytrend.interest_over_time() 
print(interest_over_time_df.head())