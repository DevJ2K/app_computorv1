import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Monomial import Monomial, MonomialError, MonomialConvertError

def test_valid_monomial_format():
		assert Monomial("X^0")._Monomial__set_monomial_coefficient() == 1
		assert Monomial("X^0")._Monomial__set_monomial_degree() == 0

		pass


def test_invalid_monomial_format():
	invalid_monomials = [
		"++5 * X^0",
		"--5*X^0",
		"+-5 * X^0",
		"+5+ * X^0",
		"+	-5 * X^0",
		"-  * X^0",
		"999..9 * X^0",
		"999.4.9 * X^0",
	]
	for monomial in invalid_monomials:
		with pytest.raises(MonomialError):
			print(monomial)
			Monomial(monomial)


def test_valid_convert_coefficient():
	assert Monomial("-X^2 ")._Monomial__set_monomial_coefficient() == -1 # type: ignore
	assert Monomial("+5 * X^0 ")._Monomial__set_monomial_coefficient() == 5 # type: ignore
	assert Monomial(" +5 * X^0 ")._Monomial__set_monomial_coefficient() == 5 #type: ignore
	assert Monomial("+545 * X^0 ")._Monomial__set_monomial_coefficient() == 545 #type: ignore
	assert Monomial("+545* X^0 ")._Monomial__set_monomial_coefficient() == 545 #type: ignore
	assert Monomial("-5*X^0")._Monomial__set_monomial_coefficient() == -5 #type: ignore
	assert Monomial(" 5*X^0")._Monomial__set_monomial_coefficient() == 5 #type: ignore
	assert Monomial(" 55.654*X^0")._Monomial__set_monomial_coefficient() == 55.654 #type: ignore

# def test_invalid_convert_coefficient():
# 	invalid_monomials = [
# 		"+-5 * X^0",
# 		"+5+ * X^0",
# 		"+	-5 * X^0",
# 		"-  * X^0",
# 		"999..9 * X^0",
# 		"999.4.9 * X^0",
# 	]
# 	for monomial in invalid_monomials:
# 		with pytest.raises(MonomialError):
# 			print(monomial)
# 			Monomial(monomial)

def test_valid_convert_degree():
	assert Monomial("+5 * X^14 ")._Monomial__set_monomial_degree() == 14 # type: ignore
	assert Monomial(" +5 * X^23 ")._Monomial__set_monomial_degree() == 23 #type: ignore
	assert Monomial("+545 * X^11 ")._Monomial__set_monomial_degree() == 11 #type: ignore
	assert Monomial("+545* X^22 ")._Monomial__set_monomial_degree() == 22 #type: ignore
	assert Monomial("-5*X^150")._Monomial__set_monomial_degree() == 150 #type: ignore
	assert Monomial(" 5*X^0")._Monomial__set_monomial_degree() == 0 #type: ignore
	assert Monomial(" 55.654*X^12")._Monomial__set_monomial_degree() == 12 #type: ignore

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
