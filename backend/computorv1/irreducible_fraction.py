def reduce_fraction(numerator: float, denominator: float) -> dict:
	min_nb = numerator if numerator < denominator else denominator
	if int(min_nb) != min_nb:
		return {
		'numerator': numerator,
		'denominator': denominator
	}
	else:
		min_nb = int(min_nb)
	print(min_nb)
	print(numerator)
	print(denominator)
	dict_nb = {
		'numerator': numerator,
		'denominator': denominator
	}
	for i in range(abs(min_nb) + 1):
		if i != 0:
			print( numerator // i)
			print( numerator / i)

			print(denominator // i)
			print(denominator / i)
		if (i != 0 and numerator // i == numerator / i and denominator // i == denominator / i):
			dict_nb['numerator'] = numerator // i
			dict_nb['denominator'] = denominator // i

	print(dict_nb)
	return dict_nb

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
