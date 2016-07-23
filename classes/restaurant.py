import requests
import json
from address import Address

headers = {'X-Access-Token': 'b6832dabf2b76e48'}

class Restaurant:

# string[]foodTypes
# boolean offersDelivery
# number deliveryPrice
# number deliveryMin
# Minimum subtotal requirement for free delivery. If the restaurant does not offer subtotal-dependent free delivery, this field will be -1. number minFreeDelivery
# boolean open
# A map of day of the week to an array of hours for which the restaurant is open. eg: {"Monday": ["06:00 AM - 12:00 AM"]} Map<string, string[]>hours
# An array of geographical zones to which the restaurant delivers DeliveryZone[]zones


#got rid of openNow because when api call is made maybe its open but then closes so for openNow should check time against hours of operation

#when initializing need to check if json actually has a value for each some restaurants do not
	def __init__(self, apiKey, name, address, city, state, zipcode, foodTypes, offersDelivery, deliveryPrice, deliveryMin, minFreeDelivery, hoursOfOperation):

		self.apiKey = apiKey
		self.name = name
		self.address = Address(address, city, state, zipcode)
		self.foodTypes = foodTypes
		self.offersDelivery = offersDelivery
		self.deliveryPrice = deliveryPrice
		self.deliveryMin = deliveryMin
		self.minFreeDelivery = minFreeDelivery
		self.hoursOfOperation = hoursOfOperation

	def getMenuItems(self):
		res_menu_url = 'https://api.eatstreet.com/publicapi/v1/restaurant/'+self.apiKey+'/menu?includeCustomizations=false'

			req = requests.get(res_menu_url, headers=headers)

			menu_items = []

			for courses in json.loads(req.content):
				for dishes in courses['items']:
					menu_items.append(dishes['name'].lower())

			return menu_items

	def isOpenNow(self):
		pass

	def isOpen(self, day, time):
		pass

	def offersDelivery(self):
		return self.offersDelivery

	def chargesForDelivery(self):
		if self.deliveryPrice > 0:
			return True
		else:
			return False

	def getDeliveryPrice(self):
		return self.deliveryPrice

	def getDeliveryMin(self):
		return self.deliveryMin




	