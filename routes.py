"""
backend routes configs
"""
import controllers
import shorten_url
import config

import uuid
import bottle
from bottle import route, template, static_file
import qrcode
from PIL import Image

@route('/')
def home():
    '''
    start page
    '''
    return "input uuid "

@route('/admin')
def admin(name='admin'):
    '''
    admin UI
    '''
    img = qrcode.make('Some data here')
    print(img)
    name = 'tdsdsest'
    return template('admin_template', name=name)


@route('/create')
def create():
    '''
    adding new secret
    '''
    shorten_url.get_short_link(config.demo_link)
    controllers.create.process_creation(config.demo_link)
    return "Added new: " + str(uuid.uuid4()) + "  "


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

