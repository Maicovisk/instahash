from typing import Counter, Text
from bs4 import BeautifulSoup as bs
from requests import get
import json
from time import sleep
from bottle import route, run, app, request as r
from bottle_cors_plugin import cors_plugin
import json

import requests
from getcookie import getCookie



params = getCookie()['cookie']




class createTags:

    def __init__(self: str) -> None:
        pass


    def Hashtags(self, text) -> json:
        global params
        try:
            vl = get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query=%23{text}', cookies=params).json()['hashtags']
        except:
            print('new cookie!!')
            params = getCookie()['cookie']
        else:
            return vl


    def search_user(self, person: str) -> json:
        return get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query=%22{person}', cookies=params).json()['users']


    def __repr__(self) -> dict:
        return params



tags = createTags()


app = app()
app.install(cors_plugin('*'))




@route('/')
def api():
    return r.method


@route('/api/<hash>')
def root(hash):
    return json.dumps([[x['hashtag']['name'], x['hashtag']['media_count']] for x in tags.Hashtags(hash)])

run()