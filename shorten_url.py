"""
works with url shortener
"""

import requests
import config
import api_key

def get_short_link(link):
    """
    retrieves the srhoten link
    """
    print()
    req_payload = {'format':'json',
            'apikey': api_key.open_api_key,
            'provider': config.open_api_provider,
            'url': link
            }

    r = requests.get('http://tiny-url.info/api/v1/create', params=req_payload)
    resp = r.json()
    print(resp)

    if(resp.state == 'ok'):
        return resp.shorturl
    else:
        ## RAISE ERROR HERE@