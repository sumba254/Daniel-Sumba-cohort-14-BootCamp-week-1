class BinarySearch(list):

	def__init__(self, a, b):
		super(BinarySearch, self).__init__(range(0, (a*b)+1, b)[1:])
		self.length = a

	def search(self, c):
		try:
			c = int(c) # if c is a string digit
			result = {}
			count = 0
			first = 0
			last = len(self) -1
			found = False

			if c > self[last] or c < self[first]:
                return dict([("count", count), ("index", -1)])

			while  first <= last and not found: #  binary search algorithm
				middle = (first + last)//2
				if self[middle] == c:
					found = True
					result['index'] = middle
				else:
					if c < self[middle]:
						last = middle - 1
						result['index'] = middle - 1
					else:
						first = midpoint + 1
						result['index'] = middle + 1
				result['count'] = count
				count +=1
			print result
			return result
		except:
			raise("Error! Check your target input")

			



	
