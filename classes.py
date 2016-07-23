import requests
import json

headers = {'X-Access-Token': 'b6832dabf2b76e48'}

class Address:

	def __init__(self, address, city, state, zipcode):
		self.address = address
		self.city = city
		self.state = state
		self.zipcode = zipcode

	def updateAddr(self, address):
		self.address = address

	def updateCity(self, city):
		self.city = city

	def updateState(self, state):
		self.state = state

	def updateZipCode(self, zipcode):
		self.zipcode = zipcode

class Restaurant:

# 	string[]foodTypes
# boolean offersDelivery
# number deliveryPrice
# number deliveryMin
# Minimum subtotal requirement for free delivery. If the restaurant does not offer subtotal-dependent free delivery, this field will be -1. number minFreeDelivery
# boolean open
# A map of day of the week to an array of hours for which the restaurant is open. eg: {"Monday": ["06:00 AM - 12:00 AM"]} Map<string, string[]>hours
# An array of geographical zones to which the restaurant delivers DeliveryZone[]zones

	def __init__(self, apiKey, name, address, city, state, zipcode):
		self.apiKey = apiKey
		self.name = name
		self.address = Address(address, city, state, zipcode)

	def getMenuItems(self):
		res_menu_url = 'https://api.eatstreet.com/publicapi/v1/restaurant/'+self.apiKey+'/menu?includeCustomizations=false'

			req = requests.get(res_menu_url, headers=headers)

			menu_items = []

			for courses in json.loads(req.content):
				for dishes in courses['items']:
					menu_items.append(dishes['name'].lower())

			return menu_items


