#!/usr/bin/env python3

import sys
from Computor import Computor

def basic_function():
	print("It's work !")

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		exit(0)
	Computor()
	basic_function()
