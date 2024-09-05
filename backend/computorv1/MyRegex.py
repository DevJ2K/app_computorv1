# class MyRegex:
# 	def __init__(self) -> None:
# 		self.monomial = r"\s*(?:(?:[-+]?\s*\d+(?:\.\d+)?\s*(?:(?:\*)?\s*[xX](?:\^\d+)?)?)|(?:[xX](?:\^\d+)?))"
# 		self.equation = r""
# 		pass

MyRegex_ = {
	'monomial': r"\s*(?:(?:[-+]?\s*(?:\d+)?(?:\.\d+)?\s*(?:(?:\*)?\s*[xX](?:\^\d+)?)?)|(?:[xX](?:\^\d+)?))",
	'monomial_1': r"\s*([-+]?)", # +5*X^2
	'monomial_2': r"\s*([-+]?)", # -X^2
	'monomial_3': r"\s*([-+]?)", # 5
	'side': r"(\s*(?:(?:[-+]?\s*(?:\d+)?(?:\.\d+)?\s*(?:(?:\*)?\s*[xX](?:\^\d+)?)?)|(?:[xX](?:\^\d+)?)))+",
	'monomial_coefficient': r"(\s*[-+]?\s*\d+(?:\.\d+)?)",
	'monomial_degree': r"(?:\*)?\s*[xX](?:\^(?P<deg>\d+))?\s*$"
}

_monomial_1_1 = r"(?:[-+]?\d+(?:\.\d+)?)?", # Match [5, -5, +5, +5.5]
_monomial_1_2 = r"(\*?[xX](?:\^\d+)?)?", # Match [..*X^3, ..X^4, ..X]

_monomial_2_1 = r"[-+]?[xX](?:\^\d+)?"

MyRegex = {
	'monomial': r"\s*(?:(?:(?:[-+]?\s*\d+(?:\.\d+)?)\s*(?:\*?\s*[xX](?:\^\d+)?)?)|(?:[-+]?\s*[xX](?:\^\d+)?))",
	# 'monomial': r"(?:[-+]?[xX](?:\^\d+)?)",
	'monomial_coefficient': r"\s*(?:(?:[-+]?\s*\d+(?:\.\d+)?)|(?:[-+]\s*(?:\d+(?:\.\d+)?)?))",
	'monomial_degree': r"(?:\*)?\s*[xX](?:\^(?P<deg>\d+))?\s*$",

	'side': r"(\s*(?:(?:(?:[-+]?\s*\d+(?:\.\d+)?)\s*(?:\*?\s*[xX](?:\^\d+)?)?)|(?:[-+]?\s*[xX](?:\^\d+)?)))+"
}
