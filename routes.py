"""
backend routes configs
"""
import controllers
import plugins
import config
import app_utils

import bottle
from bottle import Bottle, request, route, template, static_file, get, post

########################
#       main app pages
########################


##load translations
translations = app_utils.load_language('ru')

app = bottle.default_app()

@get('/')
def home():
    '''
    start page
    '''
    #working with session
    s = bottle.request.environ.get('beaker.session')
    s['test'] = 'start page visited'
    s.save()
    controllers.database.flush_expired_items()

    return template('home_page', i18n=translations)

@get('/create')
def create():
    '''
    display page to create
    '''

    #return "Added new: " + user_readable_id
    return template('create_template', i18n=translations)


@get('/secret')
def secret():
    '''
    display page to open secret
    '''
    return template('secret_view')

@get('/static/<page:re:[a-z]+>')
def static_page(page):
    '''
    display all static pages
    '''
    #page_data = controllers.static_page.read(page)
    title = 'tdsdsest'
    text = 'tdsdsest tdsdsest tdsdsesttdsdsest tdsdsest tdsdsest'
    return template('static_page', page_title=title, page_text=text, i18n=translations)



########################
#   internal api
########################

@post('/api/create')
def api_create():
    '''
    adding new secret request
    '''
    plugins.shorten_url.get_short_link(config.demo_link)
    created_data = controllers.create.process_creation(config.demo_link)
    user_readable_id = app_utils.encrypt_id(created_data['db_id'])

    ##<img src="data:image/jpeg;base64,{{qrbase64}}" width="200" height="200">
    ##, qrbase64=created_data['qrbase64'], link=user_readable_id
    # return {
    #     JSON object
    # }

@post('/api/read/<name:re:[a-z0-9]+>')
def api_read(name):
    '''
    read secret request
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
    # return {
    #     JSON object
    # }


########################
#   handling static files
########################

@get('/assets/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='assets')
