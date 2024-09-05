import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Computor import Computor

def _C(polynomial: str) -> Computor:
	return Computor(polynomial)

def test_reduce_form_all_x_solution():
    assert _C("42X^2 = 42X^2") == _C("0 = 0")
    assert _C("5X^2 + 3X^1 + 2 = 5X^2 + 3X^1 + 2") == _C("0 = 0")
    assert _C("4X^2 + 2X^1 = 4X^2 + 2X^1") == _C("0 = 0")
    assert _C("3X^2 + 2X + 1 = 3X^2 + 2X + 1") == _C("0 = 0")
    assert _C("3X^2 + 2X^1 = 0") == _C("3X^2 + 2X^1 = 0")
    assert _C("4X^2 = 4X^2") == _C("0 = 0")

def test_reduce_form_to_solve():
	assert _C("3 * X^3 - 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^1 + 1 * X^1") == _C("3 * X^3 - 9.3 * X^2 + 2 * X^1 - 5 * X^0 = 0")

	assert _C("2 * X^2 + 3 * X^1 + 4 * X^0 = 4 * X^1 + 6 * X^0") == _C("2 * X^2 - 1 * X^1 - 2 * X^0 = 0")

	assert _C("7 * X^1 + 8 * X^0 = 3 * X^1 + 4 * X^0") == _C("4 * X^1 + 4 * X^0 = 0")

	assert _C("2 * X^4 + 3 * X^3 = 3 * X^3 + 0 * X^0") == _C("2 * X^4 = 0")

	assert _C("6 * X^2 + 2 * X^1 - 4 * X^0 = 6 * X^2 + 2 * X^1 - 4 * X^0") == _C("0 = 0")

	assert _C("5 * X^0 = 3 * X^0") == _C("2 * X^0 = 0")

	assert _C("X^3 + X^2 + X^1 = 0") == _C("X^3 + X^2 + X^1 = 0")

	assert _C("3 * X^1 + 1 * X^0 = 2 * X^1 + 2 * X^0") == _C("1 * X^1 - 1 * X^0 = 0")
	assert _C("X^3 + X^2 - X^1 = 0") == _C("X^3 + X^2 - 1 * X^1 = 0")
	assert _C('0+ 2x + 7 = 0') == _C("2x + 7 = 0")

