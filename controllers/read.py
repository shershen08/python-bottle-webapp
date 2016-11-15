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

def process_reading(id):

    result = secrets.find_one({"_id": id})
    if(result != None):
        remove_selected(id)
        return result
    else:
        return 'Not found'

def remove_selected(id):
    secrets.remove({"_id":ObjectId(id)})
    pass