#!/usr/bin/env python3

import sys
from Computor import Computor
from ErrorManager import *
from Colors import *

def basic_function():
	print("It's work !")

def print_error(message: str) -> None:
	print(f"{BHRED}Error: {RESET}{BRED}{message}{RESET}")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"{BHGREEN}Usage:{RESET} {BHWHITE}./main.py {RESET}{BHCYAN}<polynomial>{RESET}")
	else:
		try:
			polynomial = Computor(sys.argv[1])
			polynomial.solve()
			print(polynomial.display_solution())
		except InvalidPolynomialError:
			print_error("The provided polynomial is invalid. Please check the format and try again.")
		except MonomialError:
			print_error("There is an issue with one or more monomials in the polynomial. Please review and correct them.")
		except MonomialConvertError:
			print_error("Could not convert one or more monomials. Ensure that the polynomial is properly formatted.")
