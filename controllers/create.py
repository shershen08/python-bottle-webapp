"""
create secret route function
"""
import uuid
import datetime
import bcrypt

import qrcode
from PIL import Image

import pymongo
from pymongo import MongoClient

import config

##init db
client = MongoClient(config.database_connection)
db = client['local']
secrets = db.secrets

password = 'JYCF^*((8oygivy))'

def process_creation(text):
    """
    generate UUID, and qu code
    """
    if(len(text) < 255):
        img = qrcode.make(text)
        print(img)
    
    #crypt_string(text)

    #uuid
    uuid_created = str(uuid.uuid4())

    db_id = db_insert(text, uuid_created)

    print('process_creation', img, uuid_created, db_id)
    return {
        'uuid': uuid_created
    }

def crypt_string(str_text):
    #http://www.mindrot.org/projects/py-bcrypt/
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    print(hashed)

def db_insert(text, secret_id):
    query = {"author": "Mike",
            "text": text,
            "sid": secret_id,
            "date": datetime.datetime.utcnow()}
    post_id = secrets.insert_one(query).inserted_id
    return post_id