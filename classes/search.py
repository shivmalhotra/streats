import requests
import json
from address import Address
from pprint import pprint

headers = {'X-Access-Token': 'b6832dabf2b76e48'}

def search(query):
	'''
	searches and passes back list of restaurants with query applied
	'''
	#grab address (TODO: grab from saved address)
	address = '131+West+Wilson+St.+Madison,+WI'
	requestUrl = 'https://api.eatstreet.com/publicapi/v1/restaurant/search?method=both&search=' + query + '&street-address=' + address
	response = requests.get(requestUrl, headers=headers)
	restaurants = json.loads(response.content)['restaurants']
	# pprint(restaurants)
	return restaurants
	
def searchByName(name):
	'''
	filters list by name. returns restaurant list matching criteria
	'''
	restaurants = search(name)
	nameMatches = []
	for r in restaurants:
		if name.lower() in r['name'].lower():
			nameMatches.append(r)
	return nameMatches

def searchByCategory(category):
	'''
	filters list by category
	'''
	nameMatches = []
	restaurants = search(category)
	for r in restaurants:
		for foodType in r['foodTypes']:
			print foodType
			if category.lower() in foodType.lower():
				nameMatches.append(r)
	return nameMatches

def searchByItem(item):
	'''
	filters list by item
	'''
	restaurants = search(item)
	nameMatches = []
	for r in restaurants:
		#grab menu items
		#if item.lower() in menu.lower()
			#nameMatches.append(r)
		pass
	return nameMatches