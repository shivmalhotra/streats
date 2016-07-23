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


