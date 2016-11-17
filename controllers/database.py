"""
handles db conection
"""
import config
import pymongo
from pymongo import MongoClient

# db connection


def database_connect():

    try:
        client = MongoClient(config.database_connection)
        db = client['local']
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



    except ValueError:
        # if no db conection
        response_status = 400
        print('if no db conection')


    return db


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
