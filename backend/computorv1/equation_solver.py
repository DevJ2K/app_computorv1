from Monomial import Monomial

def solve_polynomial_deg_0(lhs: list[Monomial], rhs: list[Monomial]) -> dict:
	if lhs == [] and lhs == []:
		return { "has_solution": True, "degree": 0 }
	return { "has_solution": False, "degree": 0 }

def solve_polynomial_deg_1(lhs: list[Monomial], rhs: list[Monomial]) -> dict:
	solution = {}
	return solution

def solve_polynomial_deg_2(lhs: list[Monomial], rhs: list[Monomial]) -> dict:
	solution = {}
	return solution
