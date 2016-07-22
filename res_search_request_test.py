import requests
import json
from pprint import pprint

headers = {'X-Access-Token': 'b6832dabf2b76e48'}

res_search_url = 'https://api.eatstreet.com/publicapi/v1/restaurant/search?'

r = requests.get(res_search_url+'method=both&street-address=95+wall+street,+new+york,+NY,+10005',headers=headers)

restaurants = json.loads(r.content)['restaurants']


# print(restaurants[2]['name'])

# res_menu_url = 'https://api.eatstreet.com/publicapi/v1/restaurant/'+str(restaurants[2]['apiKey'])+'/menu?includeCustomizations=false'

# r = requests.get(res_menu_url, headers=headers)

# menu_items = json.loads(r.content)


# pprint(menu_items[0])

desired_food = "sushi"

valid_res = []

for r in restaurants:
	for ft in [foodType.lower() for foodType in r['foodTypes']]:
		if desired_food in ft:
			valid_res.append(r)
			#break so it doesn't append twice
			break

for r in valid_res:
	print r['name']


