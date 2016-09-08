import requests
import json
import time

from pprint import pprint



class User:
    
    def __init__(self, email, password):
        url = 'https://api.eatstreet.com/publicapi/v1/signin'
        # data = {"email": "tonydurivaux@gmail.com", "password": "tototo"}
        data = {"email": email, "password": password}
        headers = {'X-Access-Token': 'c93fbcbc2fbb1386', 'Content-Type': 'application/json'}
        r = requests.post(url,data=json.dumps(data),headers=headers)

        self.apiKey = json.loads(r.content)['apiKey']


    def get_last_order():
        url = 'https://api.eatstreet.com/publicapi/v1/user/'+self.apiKey+'/orders'
        headers = {'X-Access-Token': 'c93fbcbc2fbb1386'}
        r = requests.get(url,headers=headers)
        
        return json.loads(r.content)