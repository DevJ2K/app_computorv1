import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Monomial import Monomial, MonomialError, MonomialConvertError

def test_valid_monomial_format():
		# Monomial("+ 5 * X^0 ")
		pass


def _test_invalid_monomial_format():
	invalid_monomials = [
		"++5 * X^0",
		"--5*X^0"
	]
	for monomial in invalid_monomials:
		with pytest.raises(MonomialError):
			Monomial(monomial)


def test_convert_coefficient():
	assert Monomial("+5 * X^0 ")._Monomial__set_monomial_coefficient() == 5 # type: ignore
	assert Monomial(" +5 * X^0 ")._Monomial__set_monomial_coefficient() == 5 #type: ignore
	assert Monomial("+545 * X^0 ")._Monomial__set_monomial_coefficient() == 545 #type: ignore
	assert Monomial("+545* X^0 ")._Monomial__set_monomial_coefficient() == 545 #type: ignore
	assert Monomial("-5*X^0")._Monomial__set_monomial_coefficient() == -5 #type: ignore
	assert Monomial(" 5*X^0")._Monomial__set_monomial_coefficient() == 5 #type: ignore
	assert Monomial(" 55.654*X^0")._Monomial__set_monomial_coefficient() == 55.654 #type: ignore
	pass

def test_convert_degree():
	pass

# def test_monomial_1():
# 	assert str(Monomial("+5 * X^0 ")) == '+5 * X^0'
# 	assert str(Monomial("5 * X^0")) == '+5 * X^0'
# 	assert str(Monomial("5*X^0")) == '+5 * X^0'
# 	assert str(Monomial("+ 5 * X^0 ")) == '+5 * X^0'
# 	assert str(Monomial(" + 5     * X^0 ")) == '+5 * X^0'

# def test_monomial_decimal_point():
# 	assert str(Monomial("- 9.3 * X^2 ")) == '-9.3 * X^2'
# 	assert str(Monomial("+ 9.35 * X^2 ")) == '+9.35 * X^2'
# 	assert str(Monomial("9.3 * X^2 ")) == '+9.3 * X^2'
