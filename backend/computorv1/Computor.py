from Colors import *

class Computor:
	"""Computor class : To manipulate polynomial second or lower degree equation."""


	def __init__(self, polynomial: str) -> None:
		self.polynomial = polynomial
		self.reduced_from: str | None = None
		self.x1: str | None = None
		self.x2: str | None = None
		self.__priv = 12
		self._priv = 14


	def __str__(self) -> str:
		return (f"Polynomial => {BBLACK}{self.polynomial}")


	def solve() -> str:
		pass
