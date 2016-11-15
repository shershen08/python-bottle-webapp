"""
backend routes configs
"""
import controllers
import shorten_url
import config


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
    shorten_url.get_short_link(config.demo_link)
    created_data = controllers.create.process_creation(config.demo_link)
    return "Added new: " + created_data['uuid']


@route('/secret/<name:re:[a-z]+>')
def secret(name):
    '''
    try to open secret
    '''

    ##if true - notifications.http_notify

    return "Hello :" + name + ' ' + str(uuid.uuid4())



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

