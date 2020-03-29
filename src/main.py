# Libraries
import random
import pytrends
from pytrends.request import TrendReq
import pandas as pd
import time as timer #change the name to avoid erros with time from datetime
import datetime
from datetime import datetime, date, time

# Plotting 
import matplotlib.pyplot as plt
from personal_functions import create_graphs
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
        #print(kw_list[i],kw_list[i+1])
        pytrends.build_payload(kw_list[i], cat=kw_list[i+1],timeframe='today 5-y', geo='ES', gprop='')
        interest_over_time_df = pytrends.interest_over_time() 
        #print(interest_over_time_df.head())
           #plt.figure()
        dx = interest_over_time_df.plot.line( figsize = (9,6), title =str(kw_list[i]))
        dx.set_xlabel('Date')
        dx.set_ylabel('Trends Index')
        dx.tick_params(axis='both', which='major', labelsize=13)
        plt.savefig('./output/{}.png'.format(str(kw_list[i])))
        #plt.show()

