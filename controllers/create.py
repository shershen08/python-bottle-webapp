"""
create secret route function
"""
import uuid
import datetime
import plugins

import pymongo
from pymongo import MongoClient

import config

##init db
client = MongoClient(config.database_connection)
db = client['local']
secrets = db.secrets

def process_creation(text):
    """
    generate UUID, and qu code
    """
    if(len(text) < 255):
        img = plugins.qr_code.make_img(text)
        print(img)

    #uuid
    uuid_created = str(uuid.uuid4())

    db_id = db_insert(text, uuid_created)

    print('process_creation', img, uuid_created, db_id)
    return {
        'db_id': uuid_created,
        'uuid_created' : uuid_created
    }

def db_insert(text, secret_id):
    query = {"author": "Mike",
            "text": text,
            "sid": secret_id,
            "date": datetime.datetime.utcnow()}
    post_id = secrets.insert_one(query).inserted_id
    return post_id