import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Monomial import Monomial

def test_monomial_1():
	assert str(Monomial("+5 * X^0 ")) == '+5 * X^0'
	assert str(Monomial("5 * X^0")) == '+5 * X^0'
	assert str(Monomial("+ 5 * X^0 ")) == '+5 * X^0'
	assert str(Monomial(" + 5     * X^0 ")) == '+5 * X^0'

def test_monomial_decimal_point():
	assert str(Monomial("- 9.3 * X^2 ")) == '-9.3 * X^2'
	assert str(Monomial("+ 9.35 * X^2 ")) == '+9.35 * X^2'
	assert str(Monomial("9.3 * X^2 ")) == '+9.3 * X^2'
