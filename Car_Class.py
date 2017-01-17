class Car(object):
	"""
	Car class that can be used to instantiate various vehicles
	"""
	def __init__(self, car_name="General", model="GM", car_type="saloon"):
		self.type = car_type
		self.name = car_name
		self.model = model
		self.speed = 0	
	
	def car_doors(self):
		if self.name == "porshe" or self.name == "Koenigsegg":
			return 2
		return 4

	def num_of_wheels(self):
		if self.type != "trailer":
			return 4
		return 8

	def is_saloon(self):
		if self.type == "saloon":
			return True
		return False

	def drive(self, g):
		if (self.name == "Mercedes" or self.type == "saloon") and g == 3:
			self.speed = 200
		elif (self.type == "trailer" or self.type == "trailer") and g == 7:
			self.speed == 80
		else:
			self.speed == 50
		return self


	

