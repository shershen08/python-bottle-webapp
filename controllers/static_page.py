"""
read data for static page
"""
import config
from .database import *

from bson.objectid import ObjectId

db = database_connect()
pages = db.pages

def read(page_name):

    result = pages.find_one({"name": page_name})
    if(result != None and result['sid'] != ''):
        return result