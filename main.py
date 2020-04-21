# processes
import runpy
import os
from os import listdir
from os.path import isfile, join

def main (data,context):

    processes= ("request_pytrends.py","process_files.py","upload_gcs.py","remove_files.py")
    for p in processes:
        exec(open(p).read())
        print(p, "done")

if __name__ == "__main__":
  
    main('data','context')
 