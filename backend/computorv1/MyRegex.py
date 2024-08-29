# class MyRegex:
# 	def __init__(self) -> None:
# 		self.monomial = r"\s*(?:(?:[-+]?\s*\d+(?:\.\d+)?\s*(?:(?:\*)?\s*[xX](?:\^\d+)?)?)|(?:[xX](?:\^\d+)?))"
# 		self.equation = r""
# 		pass

MyRegex = {
	'monomial': r"\s*(?:(?:[-+]?\s*\d+(?:\.\d+)?\s*(?:(?:\*)?\s*[xX](?:\^\d+)?)?)|(?:[xX](?:\^\d+)?))",
	'side': r"(\s*(?:(?:[-+]?\s*(?:\d+)?(?:\.\d+)?\s*(?:(?:\*)?\s*[xX](?:\^\d+)?)?)|(?:[xX](?:\^\d+)?)))+",
	'monomial_coefficient': r"(\s*[-+]?\s*\d+(?:\.\d+)?)",
	'monomial_degree': r"(?:\*)?\s*[xX](?:\^(?P<deg>\d+))?\s*$"
}
