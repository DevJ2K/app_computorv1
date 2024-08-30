from Monomial import Monomial

def solve_polynomial_deg_0(lhs: list[Monomial], rhs: list[Monomial]) -> dict:
	# 0 = 0
	if lhs == [] and lhs == []:
		return {
			"has_solution": True,
			"degree": 0
		}
	return {
		"has_solution": False,
		"degree": 0
	}

def solve_polynomial_deg_1(lhs: list[Monomial], rhs: list[Monomial]) -> dict:
	# ax + b = 0
	var_a: float = 0
	var_b: float = 0
	for monomial in lhs:
		if monomial.degree == 1:
			var_a = monomial.coefficient
		elif monomial.degree == 0:
			var_b = monomial.coefficient
	if var_a == 0:
		return {
			"has_solution": False,
			"degree": 1
		}
	return {
		"has_solution": True,
		"degree": 1,
		"x": (-var_b)/(var_a)
	}

	return solution

def solve_polynomial_deg_2(lhs: list[Monomial], rhs: list[Monomial]) -> dict:
	# ax^2 + bx + c = 0
	var_a: float = 0
	var_b: float = 0
	var_c: float = 0
	var_delta: float = 0
	for monomial in lhs:
		if monomial.degree == 2:
			var_a = monomial.coefficient
		elif monomial.degree == 1:
			var_b = monomial.coefficient
		elif monomial.degree == 0:
			var_c = monomial.coefficient
	var_delta = var_b ** 2 - 4 * var_a * var_c
	int_delta = int(var_delta)
	var_delta = int_delta if int_delta == var_delta else var_delta
	# print(f"a:{var_a} | b:{var_b} | c:{var_c} | delta:{var_delta}")
	if var_delta < 0:
		return {
			"has_solution": False,
			"degree": 2,
			"delta": var_delta,
		}
	x1 = ((-var_b) - var_delta ** 0.5) / (2 * var_a)
	x2 = ((-var_b) + var_delta ** 0.5) / (2 * var_a)
	int_x1 = int(x1)
	int_x2 = int(x2)
	x1 = int_x1 if int_x1 == x1 else x1
	x2 = int_x2 if int_x2 == x2 else x2

	print(x1)
	print(x2)
	if var_a < 0:
		x1, x2 = x2, x1
	return {
		"has_solution": True,
		"degree": 2,
		"delta": var_delta,
		"x1": x1,
		"x2": x2,
	}
