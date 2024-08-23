import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ParserCommand import *

class TestParsingChecker(unittest.TestCase):
	def test_is_an_equation(self):
		self.assertEqual(is_an_equation("3 = 4"), True)
		self.assertEqual(is_an_equation("3 4"), False)
		self.assertEqual(is_an_equation("3==4"), False)
		self.assertEqual(is_an_equation("0 = 3 = 4"), False)
		self.assertEqual(is_an_equation("3=4"), True)

# RUN TEST
# if __name__ == "__main__":
# 	unittest.main()

# python -m unittest -v test_ParserCommand
