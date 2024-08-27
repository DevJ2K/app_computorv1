import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ParserCommand import *


def test_valid_equation():
	assert is_an_equation("3 = 4") == True
	assert is_an_equation("3=4") == True
	assert is_an_equation("3 * X^0=4") == True
	assert is_an_equation("X^0=X^0") == True
	assert is_an_equation("-  3*X^0=   4") == True
	assert is_an_equation("3 * X^0=4*X^3 + 2 * X^3") == True
	assert is_an_equation("3 * X^0=4") == True
	assert is_an_equation("3 * X^4 = X^0") == True
	assert is_an_equation("-3 * X^4 = X^0") == True
	assert is_an_equation("-3 = X^34 + 3*X^3") == True
	assert is_an_equation("-3 = X^34 + 3*X") == True
	assert is_an_equation("0.0 + 45*x^2 + 451*x = 0") == True
	assert is_an_equation("	0.0    + 45	*	x^2 + 451	*   x = 	0") == True

def test_invalid_equation():
	assert is_an_equation("3 4") == False
	assert is_an_equation("3==4") == False
	assert is_an_equation("0 = 3 = 4") == False
	assert is_an_equation("3 * X^0=4*X^3 2 * X^3 =") == False
	assert is_an_equation("3 = ") == False
	assert is_an_equation("3 = X^") == False
	assert is_an_equation("3 * X^4 == X^0") == False
	assert is_an_equation("--3 * X^4 == X^0") == False
	assert is_an_equation("- -3 * X^4 == X^0") == False
	assert is_an_equation("- -3 * X^4 == X ^0") == False
	assert is_an_equation("- -3 * X^4 == X ^ 0") == False
	assert is_an_equation("- -3 * X^4 == X^^0") == False
	assert is_an_equation("- -3 * X^4 == X^^-10") == False
	assert is_an_equation("	0..0    + 45	*	x^2 + 451	*   x = 	0") == False
	assert is_an_equation("	0. 0    + 45	*	x^2 + 451	*   x = 	0") == False
	assert is_an_equation("	0.0    + 45	*	x^2 + 451	*   *x = 	0") == False

def test_valid_polynomial_form():
	assert is_polynomial_form("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 0") == True
	assert is_polynomial_form("5 + 4 * X^1 - 9.3 * X^2 = 0") == True
	assert is_polynomial_form("5 * X^0 + 4 * X^1 - 9.3 * X^2 = x^2") == True
	assert is_polynomial_form("5*X^0+4*X^1-9.3*X^2=0") == True
	assert is_polynomial_form("	 -5     *	 X^0   +  4 	*  X^1    -    9.3   *    X^2  = 0") == True
	assert is_an_equation("0.0 + 10*x^2 + 146*x = 0") == True
	assert is_an_equation("	0.0    + 10	*	x^2 + 146	*   x = 	0") == True

def test_invalid_polynomial_form():
	assert is_polynomial_form("5 * X^0 + 4 * X^1 - 9.3 * X^2 = ") == False
	assert is_polynomial_form("--5 * X^0 + 4 * X^1 - 9.3 * X^2 = 0") == False
	assert is_polynomial_form("5 * X^    0 + 4 * X^1 - 9.3 * X^2 = 0") == False
	assert is_polynomial_form("5 * + 4 * X^1 - 9.3 * X^2 = 0") == False
	assert is_polynomial_form("5 * X^-12 + 4 * X^1 - 9.3 * X^2 = 0") == False
	assert is_polynomial_form("5 ** X^12 + 4 * X^1 - 9.3 * X^2 = 0") == False
	assert is_polynomial_form("5 * X^12 + 4 * X^1 - 9. * X^2 = 0") == False
	assert is_polynomial_form("5 * X^12 + 4 * X^1 - 9.-43 * X^2 = 0") == False
	assert is_polynomial_form("5 * X^12 + 4 * X^1 - 9.43 * X^2 = --0^4") == False
	assert is_polynomial_form("5 * X^12 + 4 * X^1 - 9.43 * X^2  0^4") == False
	assert is_polynomial_form("5 * X^12 + 4 * X^1 - 9.43 * X^2 == 0^4") == False
	assert is_polynomial_form("5- = X^1") == False


def _strMonomialList(polynomial: str) -> str:
	string = ""
	monomial_list: list[Monomial] = convertToMonomialList(polynomial)
	for i in range(len(monomial_list)):
		coef = monomial_list[i].coefficient
		string = string + str(int(coef) if int(coef) == coef else coef)
		string += " * X^"
		string += str(monomial_list[i].degree)
		# print(monomial_list[i].degree)
		if (i + 1 < len(monomial_list)):
			string += " "
	return string

def test_valid_convert_to_monomial_list_1_item():
	assert _strMonomialList("5 * X^0") == '5 * X^0'
	assert _strMonomialList("	5 * 	X^0  ") == '5 * X^0'
	assert _strMonomialList("5") == '5 * X^0'
	assert _strMonomialList("	5.0*X^0") == '5 * X^0'
	assert _strMonomialList("5.00 * 	X^015	") == '5 * X^15'
	assert _strMonomialList("5 *       	x^130	") == '5 * X^130'
	assert _strMonomialList("5 * x^0	") == '5 * X^0'
	assert _strMonomialList("5 * X^12") == '5 * X^12'
	assert _strMonomialList("5 	*	 X^5") == '5 * X^5'
	assert _strMonomialList("55425426426426426426246246 * X^0") == '55425426426426426140917760 * X^0'
	assert _strMonomialList("5542542642642-6426426246246 * X^0") == "5542542642642 * X^0 -6426426246246 * X^0"

def test_invalid_convert_to_monomial_list_1_item():
	invalid_polynomial = [
		"5 * Xa^0",
		"5- * X^0",
		"5542542642642*6426426246246 * X^0"
	]
	for monomial in invalid_polynomial:
		with pytest.raises(InvalidPolynomialError):
			_strMonomialList(monomial)


def test_simplified_polynomial_side():
	assert simplifiedPolynomialSide(convertToMonomialList("1 * X^2 + 2 * X^2 + 4 * X^1")) == convertToMonomialList("3 * X^2 + 4 * X^1")
	assert simplifiedPolynomialSide(convertToMonomialList("1 * X^2 - 2 * X^2 - 2 * X^2  + 4 * X^1")) == convertToMonomialList("-3 * X^2 + 4 * X^1")
	assert simplifiedPolynomialSide(convertToMonomialList("2 * X^2 - 2 * X^2 + 4 * X^1")) == convertToMonomialList("0 * X^2 + 4 * X^1")

# def test_convert_to_list():
# 	assert convertToMonomialStrList("5 * X^0 + 4 * X^1 - 9.3 * X^2") == ['5*X^0', '+4*X^1 ', '-9.3*X^2']
# 	assert convertToMonomialStrList("	 5*X^0    +  	4*X^1-	 9.3*	 X^2") == ['5*X^0', '+4*X^1 ', '-9.3*X^2']
	# assert convertToMonomialStrList("5 * X^0 + 4 * X^1 - 9.3 * X^2") == ['5*X^0', '+4*X^1 ', '-9.3*X^2']
	# assert convertToMonomialStrList("5 * X^0 + 4 * X^1 - 9.3 * X^2") == ['5*X^0', '+4*X^1 ', '-9.3*X^2']

# "0.0 + 45*x^2 + 451*x = 0"

# python -m pytest -v tests/test_ParserCommand.py
# python -m pytest -v tests/test*
