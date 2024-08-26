# What's a valid polynomial ?
# - Pas d'autres characteres hormis '0->9', ' ', '*+-','^ =', 'xX'
# - len 3 min
# - 1 equal (=) avec 2 blocs et min 1 de len

from ErrorManager import ErrorManager
from Monomial import Monomial
import re

def is_an_equation(polynomial: str) -> bool:
	side_regex = r"(\s*(?:(?:[-+]?\s*\d+(?:\.\d+)?\s*(?:\*\s*[xX](?:\^\d+)?)?)|(?:[xX](?:\^\d+)?)))+"
	regex = side_regex + r"\s*=\s*" + side_regex + "$"

	match = re.match(regex, polynomial)
	if match:
		return True
	return False

	result = polynomial.split("=")
	# print(result)
	return (
		len(result) == 2
		and len(result[0]) >= 1
		and len(result[1]) >= 1
		)


def is_polynomial_form(polynomial: str) -> bool:
	if (len(polynomial) < 3):
		return False
	if (is_an_equation(polynomial) == False):
		return False

	# regex = r"(\s*[-+]?\s*\d+(?:\.\d+)?\s*(?:\*\s*X\^\d+)?)"
	regex = r"\s*(?:(?:[-+]?\s*\d+(?:\.\d+)?\s*(?:\*\s*[xX](?:\^\d+)?)?)|(?:[xX](?:\^\d+)?))"
	match = re.findall(regex, polynomial)
	if match:
		rm_equal_polynomial = polynomial.replace('=', '')
		rm_whitespace_polynomial = re.sub(r"\s", "", rm_equal_polynomial)

		# print(rm_whitespace_polynomial)
		# print(re.sub(r"\s", "",''.join(match)))
		# print(match)


		# formatted_match = [re.sub(r"\s", "", item) for item in match]
		# print(formatted_match)

		if len(rm_whitespace_polynomial) == len(re.sub(r"\s", "",''.join(match))):
			return True
		else:
			return False

	return False

# 5 * X^0 + 4 * X^1 - 9.3 * X^2 => {
# 5 * X^0
# + 4 * X^1
# - 9.3 * X^2
# }
#  1 * X^0



# def convertToMonomialList(monomial_str_list: list[str]) -> list[Monomial]:
# 	monomial_list = []
# 	for monomial_str in monomial_str_list:
# 		monomial_list.append(Monomial(monomial_str))
# 	return monomial_list

def convertToMonomialList(monomial_str_list: list[str]) -> list[Monomial]:
	pass

def convertToMonomialStrList(side: str) -> list[str]:
	pass

if (__name__ == "__main__"):
	# is_an_equation("0 = 3 = 4")
	# is_polynomial_form("5 * X^0")
	# is_polynomial_form("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 0")
	# is_polynomial_form("X^0")
	# is_polynomial_form("5 * X^0 + 4 * X^1 - 9.3 * X^2 - 5 * X^0")
	# is_polynomial_form("5 * X^0 + 4 * X^ - 9.3 * X^2 - 5 * X^0")
	# l1str = convertToMonomialStrList("5 * X^0 + 4 * X^1 - 9.3 * X^2")
	# l1 = convertToMonomialList(l1str)
	# print(l1)
	# print("==================")
	# convertToMonomialStrList("+ 4 * X^1 - 9.3 * X^2")
	# print("==================")
	# convertToMonomialStrList("+5 * X^0 + 4 * X^1 - 9.3 * X^2 - 3 * X^3")
	# print("==================")
	# convertToMonomialStrList("-5 * X^0 + 4 * X^1 - 9.3 * X^2")
	pass
