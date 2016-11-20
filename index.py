"""
secret view webapp main file
"""

##libraries
import bottle
from bottle import run
from beaker.middleware import SessionMiddleware

##app modules
import config
import app_utils
import routes

app_utils.load_language('fr')

#session configuration
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

app = SessionMiddleware(bottle.app(), session_opts)
run(app=app, host='localhost', port=config.general['port'], debug=config.general['reloader'], reloader=config.general['reloader'])