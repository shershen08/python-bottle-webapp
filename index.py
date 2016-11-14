"""
secret view webapp main file
"""

##libraries
import uuid
import qrcode
from PIL import Image
import bottle
from bottle import route, run, template, static_file

##app modules
import config
import app_utils
import app_database
import notifications

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
    return "Add new: " + str(uuid.uuid4())


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


run(host='localhost', port=config.general['port'], debug=config.general['reloader'], reloader=config.general['reloader'])