"""
secret view webapp main file
"""

##libraries
import bottle
from bottle import run
from beaker.middleware import SessionMiddleware

import cherrypy
import wsgigzip

##app modules
import config
import app_utils
import routes

app = routes.app

app_utils.load_language('fr')
app = SessionMiddleware(app, config.session_opts)

## run bottle
# run(app=app,
#     host='localhost',
#     catchall=True,
#     port=config.general['port'],
#     debug=config.general['reloader'],
#     reloader=config.general['reloader'])


application = wsgigzip.GzipMiddleware(app)

cherrypy.config.update({'server.socket_host': "0.0.0.0",
                        'server.socket_port': 8080})
cherrypy.tree.graft(application, "/")
cherrypy.engine.start()