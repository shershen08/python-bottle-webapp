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

#session configuration
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)
bottle.run(app=app)

run(host='localhost', port=config.general['port'], debug=config.general['reloader'], reloader=config.general['reloader'])