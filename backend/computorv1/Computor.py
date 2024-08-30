from Colors import *
from parser import is_polynomial_form, convertToMonomialList, simplifiedPolynomialSide
from Monomial import Monomial
from ErrorManager import *
from equation_solver import solve_polynomial_deg_0, solve_polynomial_deg_1, solve_polynomial_deg_2
import re

class Computor:
	"""Computor class : To manipulate polynomial second or lower degree equation."""

	def __init__(self, polynomial: str) -> None:
		self.polynomial: str = polynomial
		# self.polynomial: str = re.sub(r"\s*", "", polynomial)
		self.reduced_from: str | None = None

		self.lhs: list[Monomial] | None = None
		self.rhs: list[Monomial] | None = None

		self.solution: dict | None = None

		self.__initEquation()
		self.__reducePolynomial()


	def __str__(self) -> str:
		return (f"Polynomial => {BBLACK}{self.polynomial}")

	def __eq__(self, value: object) -> bool:
		if isinstance(value, Computor):
			return (
				self.lhs == value.lhs and
				self.rhs == value.rhs
			)
		return False

	def display_side(self, side: str) -> str:
		select_side: list[Monomial] = None
		if side == "left":
			select_side = self.lhs
		elif side == "right":
			select_side = self.rhs
		else:
			return None

		message: str = ""

		for item in select_side:
			if item.coefficient < 0:
				message += " - "
			elif item.coefficient > 0:
				message += " + "
			else:
				continue
			abs_coef = abs(item.coefficient)
			convert_to_int = int(abs_coef)
			if convert_to_int == abs_coef:
				message += f" {convert_to_int} * X^{item.degree} "
			else:
				message += f" {abs_coef} * X^{item.degree} "

		if message == "":
			message = "0"
		message = " ".join(message.split())
		message = message.removeprefix("+")
		message = message.removeprefix(" ")
		return message

	def display_polynomial(self, message: str = ""):
		if message != "":
			print(f"{BHCYAN}{message.ljust(30)}|{BHWHITE} {self.display_side('left')} = {self.display_side('right')}{RESET}")
		else:
			print(f"{BHWHITE}{self.display_side('left')} = {self.display_side('right')}{RESET}")
		print(31 * "=")

	def __initEquation(self) -> None:
		if (is_polynomial_form(self.polynomial) == False):
			raise InvalidPolynomialError("")
		split_polynomial = self.polynomial.split("=")

		self.lhs = convertToMonomialList(split_polynomial[0])
		self.rhs = convertToMonomialList(split_polynomial[1])

		if self.lhs is None or self.rhs is None:
			raise InvalidPolynomialError

		# Print : Init list with your params.
		# self.display_polynomial("Init with params")

		self.lhs.sort(key=lambda x: x.degree, reverse=True)
		self.rhs.sort(key=lambda x: x.degree, reverse=True)

		if (len(self.lhs) < len(self.rhs)):
			self.lhs, self.rhs = self.rhs, self.lhs

		# Print : Sort list
		# self.display_polynomial("Sort monomial by degrees")


	def __reducePolynomial(self) -> bool:
		self.lhs = simplifiedPolynomialSide(self.lhs)
		self.rhs = simplifiedPolynomialSide(self.rhs)

		# Print : Simplified expressions
		# print(self.lhs)
		# self.display_polynomial()

		for monomial_right in self.rhs:
			if monomial_right.coefficient != 0:
				monomial_right.coefficient = -monomial_right.coefficient
				# print(monomial_right)
				self.lhs.append(monomial_right)


		self.rhs.clear()
		self.lhs = simplifiedPolynomialSide(self.lhs)
		# self.display_polynomial()

		for monomial_left in self.lhs:
			for monomial_right in self.rhs:
				if monomial_left.degree == monomial_right.degree:
					if monomial_right.coefficient < 0:
						monomial_left.coefficient -= monomial_right.coefficient
						monomial_right.coefficient = 0

		return True


	def get_polynomial_degree(self) -> int:
		max_degree = 0
		if self.lhs == [] and self.rhs == []:
			return max_degree
		for monomial in self.lhs:
			if monomial.degree > max_degree:
				max_degree = monomial.degree
		return max_degree

	def get_solution(self) -> dict:
		if self.solution is None:
			print("Please solve the equation before try to get solution.")
			return {}
		return self.solution

	def display_solution(self) -> None:
		if self.solution is None:
			print("Please solve the equation before try to get solution.")
		solution_degree = self.solution['degree']
		if solution_degree == 0:
			pass
		elif solution_degree == 1:
			pass
		elif solution_degree == 2:
			pass
		else:
			pass


	def solve(self) -> str:
		polynomial_degree = self.get_polynomial_degree()
		if polynomial_degree == 0:
			self.solution = solve_polynomial_deg_0(self.lhs, self.rhs)
		elif polynomial_degree == 1:
			self.solution = solve_polynomial_deg_1(self.lhs, self.rhs)
		elif polynomial_degree == 2:
			self.solution = solve_polynomial_deg_2(self.lhs, self.rhs)
		else:
			self.solution = {
			"has_solution": None,
			"degree": polynomial_degree,
			}
			return "The polynomial degree is strictly greater than 2, I can't solve."
		return ""

if __name__ == "__main__":
	# Computor("3 * X^3	 -5     *	 X^0   +  4 	*  X^1    -    9.3   *    X^2  = 1 X^1")
	# Computor("3 * X^3 -5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1   X^1 + 1 X^1")
	# Computor("42 * X^2 = 42 * X^2")
	# Computor("5X^2 + 3X^1 + 2 = 5X^2 + 3X^1 + 2")
	# Computor("3 * X^3 -5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1   X^1 - 1 X^1")
	# Computor("1 X^1 = 3 * X^3	 -5     *	 X^0   +  4 	*  X^1    -    9.3   *    X^2")
	try:
		# computor = Computor("X^3 + X^2 - X^1 - X^0 = 0")
		computor = Computor("5 * X^0 + 4 * X^1 = 4 * X^0")
		print(f"Polynomial degree: {computor.get_polynomial_degree()}")
		# computor.get_solution()
		computor.solve()
		print(computor.get_solution())
	except Exception as error:
		print(f"Error: {error}")
