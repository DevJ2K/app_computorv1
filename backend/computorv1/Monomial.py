import re

class MonomialError(Exception):
	pass

class MonomialConvertError(Exception):
	pass

# https://docs.python.org/3/library/re.html
class Monomial:
	"""Monomial class : Item in a polynomial"""

	def __init__(self, monomial: str) -> None:
		self.monomial: str = monomial
		self.degree: int = 1
		self.coefficient: float = 0
		self.sign: str = '+'

		print(f"'{monomial}'")
		if self.__is_monomial_format():
			self.__set_monomial_coefficient()
			self.__set_monomial_degree()
		else:
			raise MonomialError("Not a monomial format.")

	def __str__(self) -> str:
		return '---------------------------------------------'
		# return f"{self.sign}{self.coefficient} * X^{self.degree}"

	def __repr__(self) -> str:
		return self.__str__()

	def __eq__(self, value: object) -> bool:
		if isinstance(value, Monomial):
			return (
				self.sign == value.sign and
                self.coefficient == value.coefficient and
                self.degree == value.degree
			)
		return False

	def __is_monomial_format(self) -> bool:
		# regex = r"([-+ \t\d]+\d+)\s*\*(\s*[xX]+\^\d+)"
		# match = re.match(regex, monomial)
		# if match:
		# 	print(f"{match.groups()}")
		# else:
		# 	print("Not a monomial")

		# Find the degree
		# match = re.search(r"[xX]'^'$", monomial)
		# if match:
		# 	print(match.group())
		# 	pass
		# else:
		# 	print("No sign found")
		return True

	def __set_monomial_coefficient(self) -> float:
		monomial = self.monomial
		# Regex groups with name
		# regex = r"^(?P<group1>[\d+-]?\d*)"

		# Find the coefficient
		# regex = r"([-+ \t\d]+\d+)"
		# regex = r"[ \t]*([-+]\d+|\d+)"
		regex = r"(\s*[-+]?\s*\d+)"
		match = re.match(regex, monomial)
		if match:
			try:
				print(f"{match.groups()} => {int(match.group())}")
				pass
			except Exception as error:
				raise MonomialConvertError("Unable to convert the value to float.")
				print(f"Error: {error}")
				pass
		else:
			print("No valid coefficient found")
		return 0.0


	def __set_monomial_degree(self) -> int:
		return 0


if __name__ == "__main__":
	print(Monomial("+5 * X^0 "))
	print(Monomial("+ * X^0 "))
	print(Monomial("++5 * X^0 "))
	print(Monomial(" +5 * X^0 "))
	print(Monomial("+545 * X^0 "))
	print(Monomial("+545* X^0 "))
	print(Monomial("-5*X^0"))
	print(Monomial("--5*X^0"))
	print(Monomial(" 5*X^0"))
	print(Monomial(" a5*X^0"))
	# print(Monomial(" 5 * X^2 "))
	# print(Monomial("+5 * X^20 "))
	# print(Monomial("- 5 * X^2 "))
	# print(Monomial("- 9.3 * X^2 "))

