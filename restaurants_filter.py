import requests
import json

headers = {'X-Access-Token': 'b6832dabf2b76e48'}

class ResFilter:

	def __init__(self, restaurants):
		self.restaurants = filter(lambda r: r['open'] == True, restaurants)

	#food type? cuisine?
	def foodType(self, food):
		results = []

		for r in self.restaurants:
			if 'foodTypes' in r:
				for ft in [_.lower() for _ in r['foodTypes']]:
					if food in ft:
						results.append(r)
						#break so it doesn't append twice
						break

		return results

	def minPrice(self, price):
		results = []

		for r in filter(lambda r: 'deliveryMin' in r, self.restaurants):
			#want to check if desired min price is at least
			#offered min price
			if price >= float(r['deliveryMin']):
				results.append(r)

		return results


	#takes too long cant think of a better way unless we cache menu items
	#but that would be bad if they change
	def foodItem(self, food):
		results = []

		for r in self.restaurants:
			res_menu_url = 'https://api.eatstreet.com/publicapi/v1/restaurant/'+str(r['apiKey'])+'/menu?includeCustomizations=false'

			req = requests.get(res_menu_url, headers=headers)

			menu_items = []

			for courses in json.loads(req.content):
				for dishes in courses['items']:
					menu_items.append(dishes['name'].lower())

			for m in menu_items:
				if food in m:
					results.append(r)
					break

		return results			


