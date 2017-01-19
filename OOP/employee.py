class Employee:

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def appy_raise(self):
		self.pay = int(self.pay* self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str ):
		first, last, pay = emp_str.split(' ')
		return cls(first, last, pay)

class Developer(Employee): # inherits from Class Employee. creates employees that are developer and the languages the specialize in.
	raise_amount = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super(Developer,self).__init__(first, last, pay)
		self.prog_lang = prog_lang

class  Manager(Employee):
	"""class manager creates managers and performs addition tasks it inherits form 
	class Employee. adds and removes employees under managers supervision"""
	def __init__(self, first, last, pay, employees = None):
		super(Manager,self).__init__(first, last, pay)
		if employees is None:
			self.employees =[]
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			priny('--->', em.fullname())
		






