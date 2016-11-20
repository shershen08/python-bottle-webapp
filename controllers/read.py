"""
read secret route function
"""

from .database import *

def process_reading(id):

    database.get_secret_item_by_id(id)
    result = secrets
    print(result)
    if(result != None and result['sid'] != ''):
        remove_selected(id)
        return result
    else:
        return 'Not found'

def remove_selected(id):
    
    database.remove_secret_item_by_id(id)
    pass