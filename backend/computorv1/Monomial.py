class Monomial:
	"""Monomial class : Item in a polynomial"""

	def __init__(self, monomial: str) -> None:
		self.degree: int = 1
		self.coefficient: float = 1
		self.sign: str = '+'

