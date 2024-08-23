class Monomial:
	"""Monomial class : Item in a polynomial"""

	def __init__(self) -> None:
		self.degree: int = 1
		self.coefficient: int = 1
		self.sign: str = '+'
