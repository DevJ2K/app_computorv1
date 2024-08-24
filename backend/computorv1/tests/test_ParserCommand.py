import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ParserCommand import *


def test_valid_equation():
	assert is_an_equation("3 = 4") == True
	assert is_an_equation("3=4") == True

def test_invalid_equation():
	assert is_an_equation("3 4") == False
	assert is_an_equation("3==4") == False
	assert is_an_equation("0 = 3 = 4") == False
	assert is_an_equation("3 = ") == False

def test_convert_to_list():
	assert convertToMonomialStrList("5 * X^0 + 4 * X^1 - 9.3 * X^2") == ['+5 * X^0 ', '+ 4 * X^1 ', '- 9.3 * X^2']

# "0.0 + 45*x^2 + 451*x = 0"

# python -m pytest -v tests/test_ParserCommand.py
# python -m pytest -v tests/test*
