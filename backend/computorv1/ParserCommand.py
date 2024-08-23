# What's a valid polynomial ?
# - Pas d'autres characteres hormis '0->9', ' ', '*+-','^ =', 'xX'
# - len 3 min
# - 1 equal (=) avec 2 blocs et min 1 de len

from ErrorManager import ErrorManager

def is_an_equation(polynomial: str) -> bool:
	result = polynomial.split("=")
	print(result)
	return (
		len(result) == 2
		and len(result[0]) >= 1
		and len(result[1]) >= 1
		)


def is_polynomial_form(polynomial: str) -> bool:
	if (len(polynomial) < 3):
		ErrorManager("Invalid polynomial format", 0, False)
		return (False)
	if (is_an_equation(polynomial) == False):
		ErrorManager("Invalid polynomial format", 0, False)
		return (False)
