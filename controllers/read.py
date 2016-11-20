"""
read secret route function
"""

from .database import *

def process_reading(id):

    dbService.get_item_by_id(id)
    result = secrets
    print(result)
    if(result != None and result['sid'] != ''):
        remove_selected(id)
        return result
    else:
        return 'Not found'

def remove_selected(id):
    
    dbService.remove_item_by_id(id)
    pass