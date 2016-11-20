"""
read data for static page
"""
import config
from .database import *

def read(page_name):

    result = dbService.get_page_item_by_id(page_name)
    if(result != None and result['sid'] != ''):
        return result