from src.math_utils import add, subtract, multiply

# --- Edge case tests for addition ---

def test_add_both_zeros():
    assert add(0, 0) == 0

def test_add_very_large_numbers():
    assert add(10**18, 10**18) == 2 * 10**18

def test_add_positive_and_negative():
    assert add(10, -3) == 7

def test_add_negative_and_positive():
    assert add(-7, 12) == 5

def test_add_small_floats():
    result = add(0.1, 0.2)
    assert abs(result - 0.3) < 1e-9

# --- Edge case tests for subtraction ---

def test_subtract_from_zero():
    assert subtract(0, 5) == -5

def test_subtract_negative_from_negative():
    assert subtract(-3, -7) == 4

def test_subtract_large_numbers():
    assert subtract(10**18, 10**17) == 9 * 10**17

def test_subtract_float_precision():
    result = subtract(1.0, 0.7)
    assert abs(result - 0.3) < 1e-9

# --- Edge case tests for multiplication ---

def test_multiply_both_zeros():
    assert multiply(0, 0) == 0

def test_multiply_by_one():
    assert multiply(42, 1) == 42

def test_multiply_by_negative_one():
    assert multiply(42, -1) == -42

def test_multiply_large_numbers():
    assert multiply(10**9, 10**9) == 10**18

def test_multiply_small_floats():
    result = multiply(0.1, 0.2)
    assert abs(result - 0.02) < 1e-9


# --- Algebraic property tests ---

def test_addition_is_commutative():
    assert add(12345, -6789) == add(-6789, 12345)


def test_subtract_is_inverse_of_add():
    a, b = 99, 33
    assert subtract(add(a, b), b) == a


def test_multiply_is_commutative():
    assert multiply(-17, 23) == multiply(23, -17)


# --- Special numeric values ---

def test_add_with_infinity():
    assert add(float("inf"), 10) == float("inf")


def test_multiply_with_infinity_and_zero_is_nan():
    result = multiply(float("inf"), 0)
    assert result != result
