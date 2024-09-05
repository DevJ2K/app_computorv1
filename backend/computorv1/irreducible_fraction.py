from parser import needToReduce

def reduce_fraction(numerator: float, denominator: float) -> dict:
	min_nb = numerator if numerator < denominator else denominator
	if int(min_nb) != min_nb:
		return {
		'numerator': numerator,
		'denominator': denominator
	}
	else:
		min_nb = int(min_nb)
	# print(min_nb)
	# print(numerator)
	# print(denominator)
	dict_nb = {
		'numerator': numerator,
		'denominator': denominator
	}
	for i in range(abs(min_nb) + 1):
		if i != 0:
			# print( numerator // i)
			# print( numerator / i)

			# print(denominator // i)
			# print(denominator / i)
			pass
		if (i != 0 and numerator // i == numerator / i and denominator // i == denominator / i):
			dict_nb['numerator'] = numerator // i
			dict_nb['denominator'] = denominator // i

	print(dict_nb)
	return dict_nb


def reduce_polynomial_degree_2(solution: dict) -> dict:
	a = solution["a"]
	b = solution["b"]
	c = solution["c"]
	delta = solution["delta"]

	result = {}

	# if delta >= 0:
	result["x1_numerator"] = f"{'- ' if b > 0 else ''}{b if b > 0 else abs(b)} - √{abs(delta)}"
	result["x1_denominator"] = f"{2 * a}"

	result["x2_numerator"] = f"{'- ' if b > 0 else ''}{b if b > 0 else abs(b)} + √{abs(delta)}"
	result["x2_denominator"] = f"{2 * a}"

	if (needToReduce(-b - abs(delta) ** 0.5) == False):
		reduce_x1_numerator = -b - abs(delta) ** 0.5
		reduce_x1 = reduce_fraction(reduce_x1_numerator, (2 * a))
		result["x1_numerator"] = reduce_x1['numerator']
		result["x1_denominator"] = reduce_x1['denominator']

	if (needToReduce(-b + abs(delta) ** 0.5) == False):
		reduce_x2_numerator = -b + abs(delta) ** 0.5
		reduce_x2 = reduce_fraction(reduce_x2_numerator, (2 * a))
		result["x2_numerator"] = reduce_x2['numerator']
		result["x2_denominator"] = reduce_x2['denominator']

	print(result)
	return result

def test_reduce_fraction():
	assert reduce_fraction(2, 4) == {'numerator': 1, 'denominator': 2}
	assert reduce_fraction(1, 6) == {'numerator': 1, 'denominator': 6}
	assert reduce_fraction(2.5, 6) == {'numerator': 2.5, 'denominator': 6}
	assert reduce_fraction(2.0, 6) == {'numerator': 1, 'denominator': 3}
	assert reduce_fraction(1, 2) == {'numerator': 1, 'denominator': 2}
	assert reduce_fraction(-1, 2) == {'numerator': -1, 'denominator': 2}
	assert reduce_fraction(-4, 8) == {'numerator': -1, 'denominator': 2}
	# assert reduce_fraction(2, 4) == {'numerator': 1, 'denominator': 2}
	# assert reduce_fraction(2, 4) == {'numerator': 1, 'denominator': 2}
	# assert reduce_fraction(2, 4) == {'numerator': 1, 'denominator': 2}

if __name__ == "__main__":
	reduce_fraction(2.0, 6)
