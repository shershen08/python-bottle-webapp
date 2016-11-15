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
    return "input of the secret "

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
    user_readable_id = app_utils.encrypt_id(created_data['uuid'])
    return "Added new: " + user_readable_id


@route('/secret/<name:re:[a-z]+>')
def secret(name):
    '''
    try to open secret
    '''
    system_readable_id = app_utils.decrypt_id(name)
    if(system_readable_id != None):
        item = controllers.read.process_reading(system_readable_id)
        if(item):
            print('record found')
        else:
            print('record not found')
    else:
        print('record not found')

    ##if true - notifications.http_notify
    return "Hello :" + name + ' '



@route('/static/<page:re:[a-z]+>')
def static(page):
    '''
    display all static pages
    '''
    page_title = 'tdsdsest'
    return "show " + page
    #return template('static_page', page_title=page_title)

@route('/help')
def help():
    #does not work
    return static_file('help.html', root='/views/')

