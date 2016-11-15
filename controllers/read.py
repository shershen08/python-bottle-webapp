"""
read secret route function
"""
import config

import pymongo
from pymongo import MongoClient

##db connection
client = MongoClient(config.database_connection)
db = client['local']
secrets = db.secrets

def process_reading(test):
    print('process_reading', test)