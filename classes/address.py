class Address:

	def __init__(self, aptnumber, address, city, state, zipcode):
		self.address = address
		self.city = city
		self.state = state
		self.zipcode = zipcode
	
	def updateApt(self, aptnumber):
		self.aptnumber = aptnumber

	def updateAddr(self, address):
		self.address = address

	def updateCity(self, city):
		self.city = city

	def updateState(self, state):
		self.state = state

	def updateZipCode(self, zipcode):
		self.zipcode = zipcode

	#dont know where to put aptnumber for query string
	def queryString():
		query = self.address + " " + self.city + " " + self.state + " " + self.zipcode
		return query.replace(" ", "+")


