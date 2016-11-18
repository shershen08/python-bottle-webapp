"""
secret view webapp main file
"""

##libraries
import json
import bottle
from bottle import run
from beaker.middleware import SessionMiddleware

##app modules
import config
import app_utils
import routes

#language file loading
def load_language(ll):
    lang_locale = 'en' if (ll == '') else ll
    lang_file_path = "./i18n/" + lang_locale + ".json"
    f = open(lang_file_path, "rb")
    data = f.read()
    f.close()
    decoded_data = data.decode('utf-8')
    json_obj = json.loads(str(decoded_data))
    #print(json_obj)
    return json_obj

load_language('fr')

#session configuration
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

app = SessionMiddleware(bottle.app(), session_opts)
run(app=app, host='localhost', port=config.general['port'], debug=config.general['reloader'], reloader=config.general['reloader'])