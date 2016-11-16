"""
backend routes configs
"""
import controllers
import plugins
import config
import app_utils

import bottle
from bottle import route, template, static_file

@route('/')
def home():
    '''
    start page
    '''
    return template('home_page')

@route('/admin')
def admin(name='admin'):
    '''
    admin UI
    '''
    name = 'tdsdsest'
    return template('admin_template', name=name)


@route('/create')
def create():
    '''
    adding new secret
    '''
    plugins.shorten_url.get_short_link(config.demo_link)
    created_data = controllers.create.process_creation(config.demo_link)
    user_readable_id = app_utils.encrypt_id(created_data['db_id'])
    #return "Added new: " + user_readable_id
    return template('create_template', qrbase64=created_data['qrbase64'], link=user_readable_id)


@route('/secret/<name:re:[a-z0-9]+>')
def secret(name):
    '''
    try to open secret
    '''
    system_readable_id = app_utils.decrypt_id(name)
    if(system_readable_id != None):
        item = controllers.read.process_reading(system_readable_id)
        if(item):
            print('record found')
            return "Hello :" + item['text'] + ' \n from ' + item['date'] + ' \n by ' + item['author']
        else:
            print('record not found')
    else:
        print('record not found')

    ##if true - notifications.http_notify
    
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


@route('/static/<page:re:[a-z]+>')
def static(page):
    '''
    display all static pages
    '''
    #page_data = controllers.static_page.read(page)
    title = 'tdsdsest'
    text = 'tdsdsest tdsdsest tdsdsesttdsdsest tdsdsest tdsdsest'
    return template('static_page', page_title=title, page_text=text)
