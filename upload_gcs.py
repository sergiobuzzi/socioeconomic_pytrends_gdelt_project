# security
import json
import sys
from dotenv import load_dotenv
load_dotenv()
# libraries
import os
import gcsfs
import pandas as pd

# this is while working out of the cloud function, for debugging or planning

# CREDENTIALS
fs = gcsfs.GCSFileSystem(token=os.getenv("TOKEN_NAME"), project=os.getenv("PROJECT_NAME"))


# Write in GCS
with fs.open(os.getenv("PROJECT_PATH")) as uploading_keywords:
    df = pd.read_csv(uploading_keywords)
fs.upload("../tmp/data_pytrends.csv",os.getenv("PROJECT_PATH"))
