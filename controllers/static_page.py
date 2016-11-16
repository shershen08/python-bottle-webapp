"""
read data for static page
"""
import config
from bson.objectid import ObjectId
import pymongo
from pymongo import MongoClient

##db connection
client = MongoClient(config.database_connection)
db = client['local']
pages = db.pages

def read(page_name):

    result = pages.find_one({"name": page_name})
    if(result != None and result['sid'] != ''):
        return result