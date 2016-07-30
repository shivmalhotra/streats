import requests
import json
from pprint import pprint

headers = {'X-Access-Token': 'b8c560b875619cb5'}

def searchForMenuItems():
	'''
	get menu items for specific restaurant
	'''
	resApiKey = '90fd4587554469b1fe2bbabe6b94d9a6068a9658ab634258'

	# res_menu_url = 'https://api.eatstreet.com/publicapi/v1/restaurant/'+resApiKey+'/menu?includeCustomizations=false'

	response = requests.get('https://api.eatstreet.com/publicapi/v1/restaurant/90fd4587554469b1fe2bbabe6b94d9a6068a9658ab634258/menu?includeCustomizations=false', headers=headers)

	print response.content

	menu_items = {}

	for courses in json.loads(response.content):
		pprint(courses)
		# for dishes in courses['items']:
			# menu_items[dishes['name'].lower()] = dishes

	# return menu_items
	# pprint(menu_items)

searchForMenuItems()