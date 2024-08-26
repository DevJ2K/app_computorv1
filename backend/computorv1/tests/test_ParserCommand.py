import sys
import os
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

def _test_valid_polynomial_form():
	assert is_polynomial_form("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 0") == True
	assert is_polynomial_form("5 + 4 * X^1 - 9.3 * X^2 = 0") == True
	assert is_polynomial_form("5 * X^0 + 4 * X^1 - 9.3 * X^2 = x^2") == True
	assert is_polynomial_form("5*X^0+4*X^1-9.3*X^2=0") == True
	assert is_polynomial_form("	 -5     *	 X^0   +  4 	*  X^1    -    9.3   *    X^2  = 0") == True

def _test_invalid_polynomial_form():
	assert is_polynomial_form("5 * X^0 + 4 * X^1 - 9.3 * X^2 = ") == False
	assert is_polynomial_form("--5 * X^0 + 4 * X^1 - 9.3 * X^2 = 0") == False
	assert is_polynomial_form("5 * X^    0 + 4 * X^1 - 9.3 * X^2 = 0") == False
	assert is_polynomial_form("5 * + 4 * X^1 - 9.3 * X^2 = 0") == False



# def test_convert_to_list():
# 	assert convertToMonomialStrList("5 * X^0 + 4 * X^1 - 9.3 * X^2") == ['5*X^0', '+4*X^1 ', '-9.3*X^2']
# 	assert convertToMonomialStrList("	 5*X^0    +  	4*X^1-	 9.3*	 X^2") == ['5*X^0', '+4*X^1 ', '-9.3*X^2']
	# assert convertToMonomialStrList("5 * X^0 + 4 * X^1 - 9.3 * X^2") == ['5*X^0', '+4*X^1 ', '-9.3*X^2']
	# assert convertToMonomialStrList("5 * X^0 + 4 * X^1 - 9.3 * X^2") == ['5*X^0', '+4*X^1 ', '-9.3*X^2']

# "0.0 + 45*x^2 + 451*x = 0"

# python -m pytest -v tests/test_ParserCommand.py
# python -m pytest -v tests/test*
