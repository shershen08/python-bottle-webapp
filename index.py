"""
secret view webapp main file
"""

##libraries
import bottle
from bottle import run

##app modules
import config
import app_utils
import app_database
import notifications
import routes

run(host='localhost', port=config.general['port'], debug=config.general['reloader'], reloader=config.general['reloader'])