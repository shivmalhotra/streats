class resFilter:

	def __init__(self, restaurants):
		self.restaurants = restaurants

	def foodType(self, desired_food):
		valid_res = []

		for r in self.restaurants:
			for ft in [foodType.lower() for foodType in r['foodTypes']]:
				if desired_food in ft:
					valid_res.append(r)
					#break so it doesn't append twice
					break

		return valid_res