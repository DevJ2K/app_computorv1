from Colors import *
from parser import is_polynomial_form, convertToMonomialList, simplifiedPolynomialSide, needToReduce
from Monomial import Monomial
from ErrorManager import *
from equation_solver import solve_polynomial_deg_0, solve_polynomial_deg_1, solve_polynomial_deg_2
from irreducible_fraction import reduce_fraction
import re

def display_status(title: str, message: str, title_color: str = BHCYAN, message_color: str = BHWHITE):
	# print(33 * "=")
	print(f"{title_color}{title.ljust(30)}|{message_color} {message}{RESET}")
	print(33 * "=")
	# print()

class Computor:
	"""Computor class : To manipulate polynomial second or lower degree equation."""

	def __init__(self, polynomial: str) -> None:
		self.polynomial: str = polynomial
		# self.polynomial: str = re.sub(r"\s*", "", polynomial)
		self.reduced_from: str | None = None

		self.lhs: list[Monomial] | None = None
		self.rhs: list[Monomial] | None = None

		self.solution: dict | None = None

		print(33 * "=")
		display_status("Input", polynomial, BHYELLOW, BHWHITE)
		self.__initEquation()
		self.__reducePolynomial()
		self.__solve()


	def __str__(self) -> str:
		return (f"Polynomial => {BBLACK}{self.polynomial}")

	def __eq__(self, value: object) -> bool:
		if isinstance(value, Computor):
			return (
				self.lhs == value.lhs and
				self.rhs == value.rhs
			)
		return False

	def display_side(self, side: str, simplified_read: bool = False) -> str:
		select_side: list[Monomial] = []
		if side == "left":
			select_side = self.lhs
		elif side == "right":
			select_side = self.rhs
		else:
			return ""

		message: str = ""

		for item in select_side: # "0x + 1 = 0"
			if item.coefficient < 0:
				message += " - "
			elif item.coefficient > 0:
				message += " + "
			else:
				continue
			abs_coef = abs(item.coefficient)
			convert_to_int = int(abs_coef)
			coef = convert_to_int if convert_to_int == abs_coef else abs_coef

			if item.degree == 0 and simplified_read:
				message += f" {coef}"
			elif item.degree == 1 and simplified_read:
				if coef == 1:
					message += f" X "
				else:
					message += f" {coef} * X "
			else:
				if coef == 1 and simplified_read:
					message += f" X^{item.degree} "
				else:
					message += f" {coef} * X^{item.degree} "

			# if convert_to_int == abs_coef:
			# 	if convert_to_int == 1:
			# 		message += f" X^{item.degree} "
			# 	else:
			# 		message += f" {convert_to_int} * X^{item.degree} "
			# else:
			# 	message += f" {abs_coef} * X^{item.degree} "

		if message == "":
			message = "0"
		message = " ".join(message.split())
		message = message.removeprefix("+")
		message = message.removeprefix(" ")
		return message

	def display_polynomial(self, message: str = "", simplified_read: bool = False):
		display_status(message, f"{self.display_side('left', simplified_read)} = {self.display_side('right', simplified_read)}", BHCYAN)

	def __initEquation(self) -> None:
		if (is_polynomial_form(self.polynomial) == False):
			raise InvalidPolynomialError("")
		split_polynomial = self.polynomial.split("=")

		self.lhs = convertToMonomialList(split_polynomial[0])
		self.rhs = convertToMonomialList(split_polynomial[1])

		if self.lhs is None or self.rhs is None:
			raise InvalidPolynomialError

		# Print : Init list with your params.
		self.display_polynomial("Initialize with parameters")

		self.lhs.sort(key=lambda x: x.degree, reverse=True)
		self.rhs.sort(key=lambda x: x.degree, reverse=True)

		if (len(self.lhs) < len(self.rhs)):
			self.lhs, self.rhs = self.rhs, self.lhs

		# Print : Sort list
		self.display_polynomial("Sort monomials by degrees")


	def __reducePolynomial(self) -> bool:
		self.lhs = simplifiedPolynomialSide(self.lhs)
		self.rhs = simplifiedPolynomialSide(self.rhs)

		self.display_polynomial("Simplify constant terms")

		for monomial_right in self.rhs:
			if monomial_right.coefficient != 0:
				monomial_right.coefficient = -monomial_right.coefficient
				# print(monomial_right)
				self.lhs.append(monomial_right)


		self.rhs.clear()

		self.display_polynomial("Move all terms to one side")

		self.lhs = simplifiedPolynomialSide(self.lhs)
		# self.display_polynomial("Simplified expressions")

		for monomial_left in self.lhs:
			for monomial_right in self.rhs:
				if monomial_left.degree == monomial_right.degree:
					if monomial_right.coefficient < 0:
						monomial_left.coefficient -= monomial_right.coefficient
						monomial_right.coefficient = 0

		self.display_polynomial("Reduced form | (Full)", False)
		self.display_polynomial("Reduced form | (Simplified)", True)

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
		# print(f"{self.display_side("left", True)} = {self.display_side("right", True)}")
		degree = self.get_polynomial_degree()
		self.solution.update({"a": 0})
		self.solution.update({"b": 0})
		self.solution.update({"c": 0})

		if self.get_polynomial_degree() == 1:
			for monomial in self.lhs:
				coef = int(monomial.coefficient) if int(monomial.coefficient) == monomial.coefficient else monomial.coefficient
				if monomial.degree == 0:
					self.solution.update({"b": coef})
				if monomial.degree == 1:
					self.solution.update({"a": coef})


			self.solution.update({"irreducible": False})
			if self.solution['has_solution']:
				self.solution.update({"irreducible": needToReduce(self.solution['x'])})
				if needToReduce(self.solution['x']):
					dict_nb = reduce_fraction(self.solution['a'], self.solution['b'])
					self.solution.update({"x_numerator": dict_nb['numerator']})
					self.solution.update({"x_denominator": dict_nb['denominator']})



		elif self.get_polynomial_degree() == 2:
			for monomial in self.lhs:
				coef = int(monomial.coefficient) if int(monomial.coefficient) == monomial.coefficient else monomial.coefficient
				if monomial.degree == 0:
					self.solution.update({"c": coef})
				if monomial.degree == 1:
					self.solution.update({"b": coef})
				if monomial.degree == 2:
					self.solution.update({"a": coef})
			self.solution.update({"irreducible": False})
			if self.solution['has_solution']:
				self.solution.update({"irreducible_x1": needToReduce(self.solution['x1'])})
				self.solution.update({"irreducible_x2": needToReduce(self.solution['x2'])})

		self.solution.update({"equation": f"{self.display_side('left', True)} = {self.display_side('right', True)}"})
		return self.solution

	def display_solution(self) -> None:
		if self.solution is None:
			print("Please solve the equation before try to get solution.")
		solution_degree = self.solution['degree']
		display_status("Polynomial degree", f"({solution_degree})", BHMAG)

		if solution_degree == 0:
			if self.solution['has_solution']:
				display_status("Solution", "All values of x are solutions.", BHGREEN)
			else:
				display_status("Solution", f"No solution exists for this constant equation : {self.display_side('left')} != {self.display_side('right')}", BHRED, BRED)

		elif solution_degree == 1:
			if self.solution['has_solution']:
				display_status("Solution", f"x = {self.solution['x']}", BHGREEN)
			else:
				display_status("Solution", f"No solution found for the equation : {self.display_side('left')} != {self.display_side('right')}, ", BHRED, BRED)

		elif solution_degree == 2:
			display_status("Delta", f"Δ = {self.solution['delta']}", BHBLUE)
			if self.solution['has_solution']:
				if self.solution['delta'] == 0:
					display_status("Number of solutions : 1", f"Δ == {self.solution['delta']}", BHGREEN)
					display_status("Solution | x", f"{self.solution['x1']}", BHGREEN)

				else:
					display_status("Number of solutions : 2", f"Δ > 0", BHGREEN)
					display_status("Solution | x1", f"{self.solution['x1']}", BHGREEN)
					display_status("Solution | x2", f"{self.solution['x2']}", BHGREEN)

			else:
				display_status("Number of solutions : 0", f"Δ < 0", BHGREEN)
				display_status("Solution | x", f"No real solution found for the quadratic equation.", BHRED, BRED)

		else:
			print(f"{BHYELLOW}The polynomial degree is strictly greater than 2, I can't solve.{RESET}")


	def __solve(self) -> None:
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

if __name__ == "__main__":
	# Computor("3 * X^3	 -5     *	 X^0   +  4 	*  X^1    -    9.3   *    X^2  = 1 X^1")
	# Computor("3 * X^3 -5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1   X^1 + 1 X^1")
	# Computor("42 * X^2 = 42 * X^2")
	# Computor("5X^2 + 3X^1 + 2 = 5X^2 + 3X^1 + 2")
	# Computor("3 * X^3 -5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1   X^1 - 1 X^1")
	# Computor("1 X^1 = 3 * X^3	 -5     *	 X^0   +  4 	*  X^1    -    9.3   *    X^2")
	try:
		# computor = Computor("42X^2 = 42X^2") # deg 0 : true
		# computor = Computor("1 = 0") # deg 0 : false
		# computor = Computor("4x + 1 = 0") # deg 1 : true
		# computor = Computor("0x + 1 = 0") # deg 1 : false
		# computor = Computor("3x^2 - 5x + 2 = 0") # deg 2 : delta > 0
		# computor = Computor("x^2 - 4x + 4 = 0") # deg 2 : delta = 0
		# computor = Computor("x^2 + 2x + 5 = 0") # deg 2 : delta < 0
		# computor = Computor("+ 2x^2 + 5 = 0+ 2x + 7") # deg 2 : delta < 0
		# computor = Computor("4x^2 + 3x^1 + 1 * X^0 = 0 -6x")
		computor = Computor("3x^2 - 5x + 2 = 0")
		from pprint import pprint
		pprint(computor.get_solution())
		# computor.display_solution(); exit(1)
	except Exception as error:
		print(f"Error: {error}")
