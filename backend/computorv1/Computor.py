from Colors import *
from ParserCommand import is_polynomial_form

class Computor:
	"""Computor class : To manipulate polynomial second or lower degree equation."""


	def __init__(self, polynomial: str) -> None:
		self.polynomial = polynomial
		self.reduced_from: str | None = None

		self.lhs: str | None = None
		self.rhs: str | None = None
		self.__priv = 12
		self._priv = 14


	def __str__(self) -> str:
		return (f"Polynomial => {BBLACK}{self.polynomial}")

	def __reducePolynomial(self) -> bool:
		polynomial = self.polynomial
		if (is_polynomial_form(polynomial) == False):
			return False
		split_polynomial = polynomial.split("=")
		lhs_str = split_polynomial[0]
		rhs_str = split_polynomial[1]

		

	def solve() -> str:
		pass
