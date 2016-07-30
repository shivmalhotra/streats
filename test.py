import requests
import json
from pprint import pprint

headers = {'X-Access-Token': '__API_EXPLORER_AUTH_KEY__'}

def searchForMenuItems():
	'''
	get menu items for specific restaurant
	'''
	resApiKey = '90fd4587554469b1fe2bbabe6b94d9a6068a9658ab634258'

	# res_menu_url = 'https://api.eatstreet.com/publicapi/v1/restaurant/'+resApiKey+'/menu?includeCustomizations=false'

	response = requests.get('https://api.eatstreet.com/publicapi/v1/restaurant/'+resApiKey+'/menu?includeCustomizations=false', headers=headers)

	# print json.loads(response.content)

	menu_items = {}

	for courses in json.loads(response.content):
		pprint(courses)
		for dishes in courses['items']:
			menu_items[dishes['name'].lower()] = dishes

	# return menu_items
	pprint(menu_items)

searchForMenuItems()