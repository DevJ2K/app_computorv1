# What's a valid polynomial ?
# - Pas d'autres characteres hormis '0->9', ' ', '*+-','^ =', 'xX'
# - len 3 min
# - 1 equal (=) avec 2 blocs et min 1 de len

from ErrorManager import ErrorManager
from Monomial import Monomial

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


# 5 * X^0 + 4 * X^1 - 9.3 * X^2 => {
# 5 * X^0
# + 4 * X^1
# - 9.3 * X^2
# }
#  1 * X^0
def convertToMonomialList(side: str) -> list[Monomial]:
	previousSign = side[0] if side[0] == "-" else "+"
	side = side.removeprefix("+")
	side = side.removeprefix("-")
	currentMonomial = ""
	str_monomial_list: list[str] = []

	i = 0
	while (i < len(side)):
		if (side[i] == "+" and i != 0):
			str_monomial_list.append(previousSign + currentMonomial)
			previousSign = "+"
			currentMonomial = ""
			i += 1
		elif (side[i] == "-" and i != 0):
			str_monomial_list.append(previousSign + currentMonomial)
			previousSign = "-"
			currentMonomial = ""
			i += 1
		else:
			currentMonomial += side[i]
			i += 1
	if (currentMonomial != ""):
		str_monomial_list.append(previousSign + currentMonomial)

	print(str_monomial_list)
	# print(str_monomial_list)
	# print(side)
	pass

if (__name__ == "__main__"):
	convertToMonomialList("5 * X^0 + 4 * X^1 - 9.3 * X^2")
	# print("==================")
	# convertToMonomialList("+ 4 * X^1 - 9.3 * X^2")
	print("==================")
	convertToMonomialList("+5 * X^0 + 4 * X^1 - 9.3 * X^2 - 3 * X^3")
	print("==================")
	convertToMonomialList("-5 * X^0 + 4 * X^1 - 9.3 * X^2")
