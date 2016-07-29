import requests
import json
import time

from pprint import pprint

def get_api_key_by_signin():
    url = 'https://api.eatstreet.com/publicapi/v1/signin'
    headers = {'X-Access-Token': 'c93fbcbc2fbb1386', 'Content-Type': 'application/json'}
    data = {"email": "tonydurivaux@gmail.com", "password": "tototo"}

    r = requests.post(url,data=json.dumps(data),headers=headers)
    apiKey = json.loads(r.content)['apiKey']
    return apiKey


def get_last_orders():
	userApiKey = get_api_key_by_signin()

	url = 'https://api.eatstreet.com/publicapi/v1/user/'+userApiKey+'/orders'
	headers = {'X-Access-Token': 'c93fbcbc2fbb1386'}
	r = requests.get(url,headers=headers)
	return json.loads(r.content)

lastOrders = get_last_orders()
pprint(lastOrders)