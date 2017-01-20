

class PSA(object):

	def __init__(self):
		self.database = []
		self.save(self.name, self.skill, self.status)

# class Add(PSA):
# 	def __init__(self, skill, self.database):
# 		# self.name = name
		# super(self.__class__, self).__init__(database)
		self.skill = skill

	def add_save(self, name, skill):
		length = len(self.database)
		dictionary = {}#initialize dic
		if length != 0:#items in the database
			for item in self.database:#
				if skill in item:
					return False
				dictionary['skill'] = skill
				dictionary['status'] = False
				return self.database.append(dictionary)
		else:
			dictionary['skill'] = skill
			dictionary['status'] = False
			return self.database.append(dictionary)

	def change_status(self, id):
		result = self.database[id]['status'] = True
		return result



# a = Add('test')
# b = Add('test')
# print a.database + b.database
		




