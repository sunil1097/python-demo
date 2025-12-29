import requests

def get_movie(base_url,params):
    return requests.get(url=base_url,params=params)