class ErrorManager:
	"""Error class : To handle all errors."""

	def __init__(self, name: str, exitCode: int = 0, exitPrograms: bool = True) -> None:
		if (name == "argc"):
			print("Number of arguments error.")
		else:
			print(f"An error has been detected about : {name}")
		if (exitPrograms):
			exit(exitCode)

class InvalidPolynomialError(Exception):
	pass

class MonomialError(Exception):
	pass

class MonomialConvertError(Exception):
	pass

class UnsolvableEquationError(Exception):
	pass
