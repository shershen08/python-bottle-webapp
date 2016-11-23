"""
handles db conection
"""
import datetime
import time
import config
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

# db connection


try:
    client = MongoClient(config.database_connection)
    connection = client['local']
#exception BottleException[s

except ValueError:
# if no db conection
    #bottle.request
    response_status = 400
    print('no db conection')
    exit()

def get_secret_item_by_id(id):
    """
    single item search
    """
    secrets = connection.secrets
    item = secrets.find_one({"_id": ObjectId(id)})
    return item

def create_new_secret(query):

    secrets = connection.secrets
    res = secrets.insert_one(query).inserted_id
    return res

def remove_secret_item_by_id(id):
    secrets = connection.secrets
    secrets.delete_one({"_id":ObjectId(id)})

def get_page_item_by_id(page_name):
    pages = connection.pages
    page = pages.find_one({"name": page_name})
    return page

def flush_expired_items():
    secrets = connection.secrets
    diff = 3600 * 1
    d = datetime.date.fromtimestamp(time.time() - diff)
    #secrets.remove({"date": {"$lt": d}}):
    return 42

def close():
    connection.close()

    #except:
    #    raise ValueError
##### - Instead of using the try/except's else block, you could simply return when it errors:
##### - http://stackoverflow.com/questions/984526/correct-way-of-handling-exceptions-in-python

	
# Instead of using the try/except's else block, you could simply return when it errors:

# def send_message(addr, to, msg):
#     ## Connect to host
#     try:
#         server = smtplib.SMTP(host) #can throw an exception
#     except smtplib.socket.gaierror:
#         return False

#     ## Login
#     try:
#         server.login(username, password)
#     except SMTPAuthenticationError:
#         server.quit()
#         return False






'''
todo:
  try:
            data = request.json()
        except:
            raise ValueError

        if data is None:
            raise 
            
            ....
            except ValueError:
        # if bad request data, return 400 Bad Request
        response.status = 400
        return
'''
