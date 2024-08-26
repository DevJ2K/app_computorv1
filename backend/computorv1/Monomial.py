# https://docs.python.org/3/library/re.html
import re
from ErrorManager import *


class Monomial:
	"""Monomial class : Item in a polynomial"""

	def __init__(self, monomial: str) -> None:
		self.monomial: str = monomial
		self.degree: int = 0
		self.coefficient: float = 1
		# self.sign: str = '+'

		if self.__is_monomial_format():
			self.__set_monomial_coefficient()
			self.__set_monomial_degree()
		else:
			raise MonomialError("Not a monomial format.")

	def __str__(self) -> str:
		print(self.monomial)
		return f"{self.coefficient} * X^{self.degree}\n======================"
		# return f"{self.monomial}\n============================"

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
		monomial = self.monomial
		regex = r"\s*(?:(?:[-+]?\s*\d+(?:\.\d+)?\s*(?:\*\s*[xX](?:\^\d+)?)?)|(?:[xX](?:\^\d+)?))\s*$"
		match = re.match(regex, monomial)
		if match:
			return True
		return False


	def __set_monomial_coefficient(self) -> float:
		monomial = self.monomial
		# Regex groups with name
		# regex = r"^(?P<group1>[\d+-]?\d*)"

		regex = r"(\s*[-+]?\s*\d+(?:\.\d+)?)"
		match = re.match(regex, monomial)
		if match:
			try:
				trim_match = re.sub(r'\s', '', match.group())
				coefficient = float(trim_match)
				# print(f"{match.groups()} => {coefficient}")
				self.coefficient = coefficient
			except Exception as error:
				raise MonomialConvertError("Unable to convert the value to float.")
				print(f"Error: {error}")
		else:
			print("No valid coefficient found")
		return self.coefficient


	def __set_monomial_degree(self) -> int:
		monomial = self.monomial
		regex = r"\*\s*[xX](?:\^(?P<deg>\d+))?\s*$"
		match = re.search(regex, monomial)
		if match:
			deg_str = match.groups("deg")[0]
			if (deg_str == "deg"):
				self.degree = 1
				# print(f"DEGREES : {self.degree}")
			else:
				try:
					self.degree = int(deg_str)
					# print(f"DEGREES : {self.degree}")
				except:
					raise MonomialConvertError("Unable to convert the value to int.")
		else:
			print("No degree found")
		return self.degree


if __name__ == "__main__":
	# print(int("-    5"))
	print(Monomial("+  5 * X^1 "))
	# print(Monomial("+ * X^0 "))
	# print(Monomial("++5 * X^0 "))
	print(Monomial(" +5 * X^3 "))
	print(Monomial(" +5.4 * X^4 "))
	print(Monomial("+545 * X^12 "))
	print(Monomial("+545* X^43 "))
	print(Monomial("-5*X^0"))
	# print(Monomial("--5*X^0"))
	print(Monomial(" 5*X^0"))
	print(Monomial(" 5"))
	print(Monomial(" 5 * X"))
	# print(Monomial(" a5*X^0"))
	# print(Monomial(" 5 * X^2 "))
	# print(Monomial("+5 * X^20 "))
	# print(Monomial("- 5 * X^2 "))
	# print(Monomial("- 9.3 * X^2 "))

