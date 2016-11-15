"""
app-wide utils
"""
import bcrypt
import api_key

password = api_key.encryption_salt

def encrypt_id(db_id):
    return db_id

def decrypt_id(url_id):
    return url_id

def crypt_string(str_text):
    #http://www.mindrot.org/projects/py-bcrypt/
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    print(hashed)