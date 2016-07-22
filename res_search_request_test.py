import requests
import json

headers = {'X-Access-Token': 'b6832dabf2b76e48'}

res_search_url = 'https://api.eatstreet.com/publicapi/v1/restaurant/search?'

r = requests.get(res_search_url+
'method=both&street-address=95+wall+street,+new+york,+NY,+10005',
headers=headers)

restaurants = json.loads(r.content)['restaurants']

print(restaurants[0]['name'])