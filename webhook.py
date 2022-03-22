from sqlite3 import apilevel
import requests
import json

webhook_url = 'https://webhook.site/364e412a-9693-4141-8f21-4f8e8434046b'

data =  { 'name' 'Instance', 'Instance URL' 'test url'}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-type': 'application/json'})