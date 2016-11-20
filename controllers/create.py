"""
create secret route function
"""
import uuid
import datetime
import plugins
from .database import *

def process_creation(text):
    """
    generate UUID, and qu code
    """
    if(len(text) < 255):
        imgqr = plugins.qr_code.make_img(text)

    #uuid
    uuid_created = str(uuid.uuid4())

    db_id = db_insert(text, uuid_created)

    print('process_creation', uuid_created, db_id)
    return {
        'db_id': db_id,
        'uuid_created' : uuid_created,
        'qrbase64': imgqr
    }

def db_insert(text, secret_id):
    query = {"author": "Mike",
             "text": text,
             "sid": secret_id,
             "date": datetime.datetime.utcnow()}
    post_id = dbService.create_new(query)
    return post_id
