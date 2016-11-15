"""
read secret route function
"""
import config
from bson.objectid import ObjectId
import pymongo
from pymongo import MongoClient

##db connection
client = MongoClient(config.database_connection)
db = client['local']
secrets = db.secrets

def process_reading(id):

    result = secrets.find_one({"_id": ObjectId(id)})
    print(result)
    if(result != None and result['sid'] != ''):
        remove_selected(id)
        return result
    else:
        return 'Not found'

def remove_selected(id):
    secrets.delete_one({"_id":ObjectId(id)})
    pass