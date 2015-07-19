import unittest
import owls

class OwlTests(unittest.TestCase):
	def test_set(self):
		self.assertEqual(owls.empty_set(), set())
	def test_dict(self):
		self.assertEqual(owls.empty_dict(), dict())
	def test_list(self):
		self.assertEqual(owls.empty_list(), list())
	def test_tuple(self):
		self.assertEqual(owls.empty_tuple(), tuple())

if __name__=='__main__':
	unittest.main()
