# What's a valid polynomial ?
# - Pas d'autres characteres hormis '0->9', ' ', '*+-','^ =', 'xX'
# - len 3 min
# - 1 equal (=) avec 2 blocs et min 1 de len


def is_an_equation(polynomial: str) -> bool:
	result = polynomial.split()
	return (
		len(result) == 2
		and len(result[0]) > 1
		and len(result[1]) > 1
		)


def is_polynomial_form(polynomial: str) -> bool:

	pass
