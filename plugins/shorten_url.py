"""
works with url shortener
"""

import requests
import config
import api_key

tu_api = dict(
    create = 'http://tiny-url.info/api/v1/create'
)

def get_short_link(link):
    """
    retrieves the srhoten link
    """
    req_payload = {'format':'json',
            'apikey': api_key.open_api_key,
            'provider': config.open_api_provider,
            'url': link
            }

    r = requests.get(tu_api['create'], params=req_payload)
    resp = r.json()
    print(resp)

    if(resp['state'] == 'ok'):
        return resp['shorturl']
    #else:
        # RAISE ERROR HERE