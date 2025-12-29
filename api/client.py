import requests

def get(base_url,params):
    return requests.get(url=base_url,params=params)