import requests

def http_notify():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    print(r.status_code)
    pass