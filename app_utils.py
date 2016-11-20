"""
app-wide utils
"""
import bcrypt
import api_key
import json

password = api_key.encryption_salt

def encrypt_id(db_id):
    return db_id

def decrypt_id(url_id):
    return url_id

def crypt_string(str_text):
    #http://www.mindrot.org/projects/py-bcrypt/
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    print(hashed)


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