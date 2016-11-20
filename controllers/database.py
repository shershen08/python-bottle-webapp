"""
handles db conection
"""
import config
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

# db connection

class dbService:
    
    def __init__(self):
        self.connection = database_connect()
        self.data = []
    
    def database_connect():
        """
        setup
        """
        try:
            client = MongoClient(config.database_connection)
            db = client['local']

        except ValueError:
        # if no db conection
            response_status = 400
            print('no db conection')
    
    return db

    def get_item_by_id(id):
        """
        single item search
        """
        secrets = self.connection.secrets
        item = secrets.find_one({"_id": ObjectId(id)})
        return item

    def create_new(id):
        secrets = self.connection.secrets
        res = secrets.insert_one(query).inserted_id
        return res

    def remove_item_by_id(id):
        secrets = self.connection.secrets
        secrets.delete_one({"_id":ObjectId(id)})

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
