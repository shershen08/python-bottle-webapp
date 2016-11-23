"""
secret view webapp main file
"""

##libraries
import bottle
from beaker.middleware import SessionMiddleware

import cherrypy
import wsgigzip

##app modules
import config
import app_utils
import routes

__app__ = routes.app

app = SessionMiddleware(__app__, config.session_opts)

## run bottle
# run(app=app,
#     host='localhost',
#     catchall=True,
#     port=config.general['port'],
#     debug=config.general['reloader'],
#     reloader=config.general['reloader'])

application = wsgigzip.GzipMiddleware(app)

cherrypy.config.update({'server.socket_host': 'localhost',
                        'server.socket_port': config.general['port']})
cherrypy.tree.graft(application, "/")
cherrypy.engine.start()