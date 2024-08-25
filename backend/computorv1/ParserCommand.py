# What's a valid polynomial ?
# - Pas d'autres characteres hormis '0->9', ' ', '*+-','^ =', 'xX'
# - len 3 min
# - 1 equal (=) avec 2 blocs et min 1 de len

from ErrorManager import ErrorManager
from Monomial import Monomial

def is_an_equation(polynomial: str) -> bool:
	result = polynomial.split("=")
	# print(result)
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
	return (True)

# 5 * X^0 + 4 * X^1 - 9.3 * X^2 => {
# 5 * X^0
# + 4 * X^1
# - 9.3 * X^2
# }
#  1 * X^0



def convertToMonomialList(monomial_str_list: list[str]) -> list[Monomial]:
	monomial_list = []
	for monomial_str in monomial_str_list:
		monomial_list.append(Monomial(monomial_str))
	return monomial_list

def convertToMonomialStrList(side: str) -> list[str]:
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
	return (str_monomial_list)


if (__name__ == "__main__"):
	l1str = convertToMonomialStrList("5 * X^0 + 4 * X^1 - 9.3 * X^2")
	l1 = convertToMonomialList(l1str)
	print(l1)
	# print("==================")
	# convertToMonomialStrList("+ 4 * X^1 - 9.3 * X^2")
	print("==================")
	# convertToMonomialStrList("+5 * X^0 + 4 * X^1 - 9.3 * X^2 - 3 * X^3")
	# print("==================")
	# convertToMonomialStrList("-5 * X^0 + 4 * X^1 - 9.3 * X^2")
