class Monomial:
	"""Monomial class : Item in a polynomial"""

	def __init__(self, monomial: str) -> None:
		self.degree: int = 1
		self.coefficient: float = 1
		self.sign: str = '+'


	def __str__(self) -> str:
		return f"{self.sign}{self.coefficient} * X^{self.degree}"

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


if __name__ == "__main__":
	print(Monomial("+5 * X^0 ")) # '+5 *X^0'
	print(Monomial(" 5 * X^2 ")) # '+5 *X^0'
	print(Monomial("+5 * X^20 ")) # '+5 *X^0'
	print(Monomial("- 5 * X^2 ")) # '+5 *X^0'
	print(Monomial("- 9.3 * X^2 ")) # '+5 *X^0'

