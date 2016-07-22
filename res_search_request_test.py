import requests
import json
import time

from pprint import pprint
from restaurants_filter import ResFilter


headers = {'X-Access-Token': 'b6832dabf2b76e48'}

res_search_url = 'https://api.eatstreet.com/publicapi/v1/restaurant/search?'

r = requests.get(res_search_url+'method=both&street-address=95+wall+street,+new+york,+NY,+10005',headers=headers)

restaurants = json.loads(r.content)['restaurants']



# res_menu_url = 'https://api.eatstreet.com/publicapi/v1/restaurant/'+str(restaurants[2]['apiKey'])+'/menu?includeCustomizations=false'

# r = requests.get(res_menu_url, headers=headers)

# menu_items = json.loads(r.content)

# pprint(menu_items[0])

pprint(restaurants[0])

print '-------------------------------'


restaurant_filter = ResFilter(restaurants)

for r in restaurant_filter.minPrice(5):
	print r['name']


print '-------------------------------'

t = time.time()

for r in restaurant_filter.foodItem("pad thai"):
	print r['name']

print '-------------------------------'

print time.time() - t


	


