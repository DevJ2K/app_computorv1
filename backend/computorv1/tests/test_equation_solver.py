import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from equation_solver import *
from Computor import Computor

def test_valid_polynomial_deg_0():
	# ["equation", "expected"]
	testing_value = [
		["0 = 0", {"has_solution": True, "degree": 0}],
		["42X^2 = 42X^2", {"has_solution": True, "degree": 0}],
		["42X^5 = 42X^5", {"has_solution": True, "degree": 0}],
		["42X^0 = 42X^0", {"has_solution": True, "degree": 0}],
		["X^0 = X^0", {"has_solution": True, "degree": 0}],
		["X^0 + 2X^2 = X^0 + 2X^2", {"has_solution": True, "degree": 0}],
		["1 = 1", {"has_solution": True, "degree": 0}],
		["-3 = -3", {"has_solution": True, "degree": 0}],
		["7 + 2 = 9", {"has_solution": True, "degree": 0}],
		["100 = 100", {"has_solution": True, "degree": 0}],
		["5 * X^0 = 5 * X^0", {"has_solution": True, "degree": 0}],
		["2 + 3 = 5", {"has_solution": True, "degree": 0}],
		["10 - 2 = 8", {"has_solution": True, "degree": 0}],
		["X^0 + X^0 = 2 * X^0", {"has_solution": True, "degree": 0}],
	]
	for test in testing_value:
		print("CURRENT TEST =>", test[0])
		instance = Computor(test[0])
		result = solve_polynomial_deg_0(instance.lhs, instance.rhs)
		assert result == test[1], f"Failed for equation: {test[0]} with result: {result}"

def test_invalid_polynomial_deg_0():
	# ["equation", "expected"]
	testing_value = [
		["1 = 0", {"has_solution": False, "degree": 0}],
		["42 = 32X^0", {"has_solution": False, "degree": 0}],
		["3 = 5", {"has_solution": False, "degree": 0}],
		["10 = -10", {"has_solution": False, "degree": 0}],
		["7 + 1 = 9", {"has_solution": False, "degree": 0}],
		["20 = 21", {"has_solution": False, "degree": 0}],
		["100 = 101", {"has_solution": False, "degree": 0}],
		["5 * X^0 = 6 * X^0", {"has_solution": False, "degree": 0}],
		["2 + 2 = 5", {"has_solution": False, "degree": 0}],
		["10 - 1 = 8", {"has_solution": False, "degree": 0}],
		["0 = 1", {"has_solution": False, "degree": 0}],
		["50 = 49", {"has_solution": False, "degree": 0}],
		["X^0 = 0", {"has_solution": False, "degree": 0}],
		["20 + 1 = 19", {"has_solution": False, "degree": 0}],
		["X^0 + X^0 = X^0", {"has_solution": False, "degree": 0}],
	]
	for test in testing_value:
		print("CURRENT TEST =>", test[0])
		instance = Computor(test[0])
		result = solve_polynomial_deg_0(instance.lhs, instance.rhs)
		assert result == test[1], f"Failed for equation: {test[0]} with result: {result}"




def test_valid_polynomial_deg_1():
	# ["equation", "expected"]
	testing_value = [
		["4x + 1 = 0", {"has_solution": True, "degree": 1, "x": -0.25}],
		["2x - 4 = 0", {"has_solution": True, "degree": 1, "x": 2}],
		["-3x + 9 = 0", {"has_solution": True, "degree": 1, "x": 3}],
		["5x - 5 = 0", {"has_solution": True, "degree": 1, "x": 1}],
		["x - 7 = 0", {"has_solution": True, "degree": 1, "x": 7}],
		["6x + 2 = 0", {"has_solution": True, "degree": 1, "x": -1/3}],
		["10x + 5 = 0", {"has_solution": True, "degree": 1, "x": -0.5}],
		["x + 100 = 0", {"has_solution": True, "degree": 1, "x": -100}],
		["0.5x - 1 = 0", {"has_solution": True, "degree": 1, "x": 2}],
		["8x + 16 = 0", {"has_solution": True, "degree": 1, "x": -2}],
		["-2x + 8 = 0", {"has_solution": True, "degree": 1, "x": 4}],
		["7x + 21 = 0", {"has_solution": True, "degree": 1, "x": -3}],
		["3.5x - 7 = 0", {"has_solution": True, "degree": 1, "x": 2}],
		["9x - 3 = 0", {"has_solution": True, "degree": 1, "x": 1/3}],
		["-4x - 8 = 0", {"has_solution": True, "degree": 1, "x": -2}],
	]
	for test in testing_value:
		print("CURRENT TEST =>", test[0])
		instance = Computor(test[0])
		result = solve_polynomial_deg_1(instance.lhs, instance.rhs)
		assert result == test[1], f"Failed for equation: {test[0]} with result: {result}"

def test_invalid_polynomial_deg_1():
	# ["equation", "expected"]
	testing_value = [
		["0x + 1 = 0", {"has_solution": False, "degree": 1}],
		["0x + 13 = 0", {"has_solution": False, "degree": 1}],
		["0x - 7 = 0", {"has_solution": False, "degree": 1}],
		["0x + 100 = 0", {"has_solution": False, "degree": 1}],
		["0x + 50 = 0", {"has_solution": False, "degree": 1}],
		["0x - 1 = 0", {"has_solution": False, "degree": 1}],
		["0x + 25 = 0", {"has_solution": False, "degree": 1}],
		["0x + 8 = 0", {"has_solution": False, "degree": 1}],
		["0x - 10 = 0", {"has_solution": False, "degree": 1}],
		["0x + 30 = 0", {"has_solution": False, "degree": 1}],
		["0x + 99 = 0", {"has_solution": False, "degree": 1}],
		["0x - 0.001 = 0", {"has_solution": False, "degree": 1}],
		["0x + 0.5 = 0", {"has_solution": False, "degree": 1}],
		["0x + 6.283 = 0", {"has_solution": False, "degree": 1}],
		["0x + 42 = 0", {"has_solution": False, "degree": 1}],
	]
	for test in testing_value:
		print("CURRENT TEST =>", test[0])
		instance = Computor(test[0])
		result = solve_polynomial_deg_1(instance.lhs, instance.rhs)
		assert result == test[1], f"Failed for equation: {test[0]} with result: {result}"





def test_polynomial_deg_2_delta_upper_0():
	# ["equation", "expected"]
	testing_value = [
		["3x^2 - 5x + 2 = 0", {"has_solution": True, "degree": 2, "delta": 1, "x1": 2/3, "x2": 1}],
		["x^2 - 3x + 2 = 0", {"has_solution": True, "degree": 2, "delta": 1, "x1": 1, "x2": 2}],
		["-x^2 + 4x - 3 = 0", {"has_solution": True, "degree": 2, "delta": 4, "x1": 1, "x2": 3}],
		["x^2 - 10x + 9 = 0", {"has_solution": True, "degree": 2, "delta": 64, "x1": 1, "x2": 9}],
		["2x^2 - 100x + 98 = 0", {"has_solution": True, "degree": 2, "delta": 9216, "x1": 1, "x2": 49}],
		["x^2 - 9 = 0", {"has_solution": True, "degree": 2, "delta": 36, "x1": -3, "x2": 3}],
		["x^2 - 2x - 3 = 0", {"has_solution": True, "degree": 2, "delta": 16, "x1": -1, "x2": 3}],
		["2x^2 - 4x - 6 = 0", {"has_solution": True, "degree": 2, "delta": 64, "x1": -1, "x2": 3}],
		["5x^2 - 3x - 2 = 0", {"has_solution": True, "degree": 2, "delta": 49, "x1": -0.4, "x2": 1}],
		["4x^2 - 12x + 5 = 0", {"has_solution": True, "degree": 2, "delta": 64, "x1": 0.5, "x2": 2.5}],
		["6x^2 - x - 1 = 0", {"has_solution": True, "degree": 2, "delta": 25, "x1": -1/3, "x2": 1/2}],
		["x^2 - 7x + 10 = 0", {"has_solution": True, "degree": 2, "delta": 9, "x1": 2, "x2": 5}],
		["9x^2 - 12x + 4 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": 2/3, "x2": 2/3}],
		["x^2 - 5x + 6 = 0", {"has_solution": True, "degree": 2, "delta": 1, "x1": 2, "x2": 3}],
		["2x^2 - 7x + 3 = 0", {"has_solution": True, "degree": 2, "delta": 25, "x1": 0.5, "x2": 3}],
	]
	for test in testing_value:
		print("CURRENT TEST =>", test[0])
		instance = Computor(test[0])
		result = solve_polynomial_deg_2(instance.lhs, instance.rhs)
		assert result == test[1], f"Failed for equation: {test[0]} with result: {result} | except: {test[1]}"


def test_polynomial_deg_2_delta_equal_0():
	# ["equation", "expected"]
	testing_value = [
		["x^2 - 4x + 4 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": 2, "x2": 2}],
		["0.5x^2 - x + 0.5 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": 1, "x2": 1}],
		["4x^2 - 4x + 1 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": 0.5, "x2": 0.5}],
		["x^2 - 6x + 9 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": 3, "x2": 3}],
		["x^2 + 2x + 1 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": -1, "x2": -1}],
		["2x^2 - 4x + 2 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": 1, "x2": 1}],
		["9x^2 - 12x + 4 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": 2/3, "x2": 2/3}],
		["3x^2 + 6x + 3 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": -1, "x2": -1}],
		["16x^2 - 8x + 1 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": 0.25, "x2": 0.25}],
		["25x^2 - 10x + 1 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": 0.2, "x2": 0.2}],
		["x^2 + 10x + 25 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": -5, "x2": -5}],
		["4x^2 - 12x + 9 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": 1.5, "x2": 1.5}],
		["x^2 + 14x + 49 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": -7, "x2": -7}],
		["x^2 - 2x + 1 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": 1, "x2": 1}],
		["x^2 - 18x + 81 = 0", {"has_solution": True, "degree": 2, "delta": 0, "x1": 9, "x2": 9}],
	]
	for test in testing_value:
		print("CURRENT TEST =>", test[0])
		instance = Computor(test[0])
		result = solve_polynomial_deg_2(instance.lhs, instance.rhs)
		assert result == test[1], f"Failed for equation: {test[0]} with result: {result}"


def test_polynomial_deg_2_delta_lower_0():
	# ["equation", "expected"]
	testing_value = [
		["x^2 + 2x + 5 = 0", {"has_solution": False, "degree": 2, "delta": -16}],
		["x^2 + x + 1 = 0", {"has_solution": False, "degree": 2, "delta": -3}],
		["x^2 - 2x + 5 = 0", {"has_solution": False, "degree": 2, "delta": -16}],
		["x^2 + 6x + 10 = 0", {"has_solution": False, "degree": 2, "delta": -4}],
		["2x^2 + 2x + 3 = 0", {"has_solution": False, "degree": 2, "delta": -20}],
		["3x^2 + 4x + 5 = 0", {"has_solution": False, "degree": 2, "delta": -44}],
		["x^2 + 10x + 26 = 0", {"has_solution": False, "degree": 2, "delta": -4}],
		["2x^2 + x + 2 = 0", {"has_solution": False, "degree": 2, "delta": -15}],
		["5x^2 + 3x + 2 = 0", {"has_solution": False, "degree": 2, "delta": -31}],
		["x^2 + 8x + 17 = 0", {"has_solution": False, "degree": 2, "delta": -4}],
		["4x^2 + 4x + 5 = 0", {"has_solution": False, "degree": 2, "delta": -64}],
		["x^2 - x + 5 = 0", {"has_solution": False, "degree": 2, "delta": -19}],
		["3x^2 + 2x + 2 = 0", {"has_solution": False, "degree": 2, "delta": -20}],
		["2x^2 + 6x + 10 = 0", {"has_solution": False, "degree": 2, "delta": -44}],
	]
	for test in testing_value:
		print("CURRENT TEST =>", test[0])
		instance = Computor(test[0])
		result = solve_polynomial_deg_2(instance.lhs, instance.rhs)
		assert result == test[1], f"Failed for equation: {test[0]} with result: {result}"
