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
	filters list by name
	'''
	restaurants = search(name)

def searchByCategory(category):
	'''
	filters list by category
	'''
	restaurants = search(category)

def searchByItem(item):
	'''
	filters list by item
	'''
	restaurants = search(item)
