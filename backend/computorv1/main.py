#!/usr/bin/env python3

import sys
from Computor import Computor
from ErrorManager import ErrorManager

def basic_function():
	print("It's work !")

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		ErrorManager("argc", 1)
	polynomial = Computor("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
	print(polynomial._priv)
	print(polynomial._Computor__priv)
	print(polynomial)
