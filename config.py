#####
## application
#####
general = dict(
    port = 9999,
    reloader = True,
    app_name =  'Secret share app'
)
demo_link = 'https://github.com/shershen08/es6-webpack-starter'


#session configuration
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

#####
## database
#####
database_connection = 'mongodb://localhost:27017/'

#####
## plugins
#####
open_api_provider = 'goo_gl'

