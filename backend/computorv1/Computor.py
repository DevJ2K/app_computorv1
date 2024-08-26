from Colors import *
from ParserCommand import is_polynomial_form, convertToMonomialList
from Monomial import Monomial
from ErrorManager import *

class Computor:
	"""Computor class : To manipulate polynomial second or lower degree equation."""

	def __init__(self, polynomial: str) -> None:
		self.polynomial = polynomial
		self.reduced_from: str | None = None

		self.lhs: list[Monomial] | None = None
		self.rhs: list[Monomial] | None = None

		self.__initEquation()


	def __str__(self) -> str:
		return (f"Polynomial => {BBLACK}{self.polynomial}")

	def __initEquation(self) -> None:
		if (is_polynomial_form(self.polynomial) == False):
			raise InvalidPolynomialError
		split_polynomial = self.polynomial.split("=")

		self.lhs = convertToMonomialList(split_polynomial[0]);
		self.rhs = convertToMonomialList(split_polynomial[1]);

		if self.lhs is None or self.rhs is None:
			raise InvalidPolynomialError

		print(self.lhs)
		print(self.rhs)



	def __reducePolynomial(self) -> bool:
		polynomial = self.polynomial
		if (is_polynomial_form(polynomial) == False):
			return False
		split_polynomial = polynomial.split("=")
		lhs_str = split_polynomial[0]
		rhs_str = split_polynomial[1]
		return True



	def solve(self) -> str:
		return ""

if __name__ == "__main__":
	Computor("	 -5     *	 X^0   +  4 	*  X^1    -    9.3   *    X^2  = 0")
