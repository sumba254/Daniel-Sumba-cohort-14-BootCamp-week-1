import unittest
from primes.py import getPrimes

class primesTestCase(unittest.TestCase):
	"""Test for primes.py"""
	def test_is_five_prime(self):
		""" chescks if five is a prime"""
		self.assertTrue(getPrimes(5))
	
	def test_is_two_prime(self):
		""" checks if two is  a prime"""
		self.assertTrue(getPrimes(5))
	
	def test_if_zero_not_a_prime(self):
		"""checks if zero is not a prime"""
		self.assertFalse(getPrimes(0))
	def test_seven_is_a_prime(self):
		"""checks if seven is a prime number"""
		self.assertTrue(getPrimes(7))
	def test_if_six_not_a_prime(self):
		"""checks if six is not a prime number"""
		self.assertFalse(getPrimes(5))
	
if __name__ == '__main__':
	unittest.main()