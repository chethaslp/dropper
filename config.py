"""
CONFIG FILE

* ADD YOUR CREDS HERE BEFORE YOU CONTINUE.
* Most PaaS supports environment variables and secret files to be added.
  You can either add these variables in your environmental variables (prefered)
  Or, if you are using it locally add it directly below.

* You should have a cred.json file downloaded from firebase console.

* Set the following environment variables:
    PASSWORD : your password
    
    CRED_FILE : your firebase cred file URL. Do not set if its in the root folder. Upload it as a 'secret file' in your Server/PaaS.
    STRG_BKT : your firebase storage bucket URL
    STRG_DB : your firebase database URL

    IP_API : Go to ipdata.co, create an account, and add your api here.
          (This is required for capturing user IP and IP Location)

    VIEW URL: your login url (change it accordingly)
    SECRET_KEY: used for session storage (any random strong password could be added) [trivial]

"""

import os
from dotenv import load_dotenv

load_dotenv()

def excep():
  raise Exception("Please set all required variables.")

CRED_FILE = os.environ.get("CRED_FILE") or "cred.json"

STORAGE_URL = {'storageBucket': os.environ.get("STRG_BKT") or excep(),
                'databaseURL': os.environ.get("STRG_DB") or excep()}
PASSWORD = os.environ.get("PASSWORD") or "admin123"
VIEW_URL = os.environ.get("VIEW_URL") or "/view/admin"
SECRET_KEY = os.environ.get("SECRET_KEY") or "chcnjshcbsjyubv8"
IP_API = os.environ.get("IP_API") or excep()