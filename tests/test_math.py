from src.math_utils import add, subtract, multiply

# --- Addition tests ---

def test_add():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

# --- Subtraction tests ---

def test_subtract():
    assert subtract(10, 4) == 6

def test_subtract_negative_result():
    assert subtract(3, 7) == -4

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_subtract_same_numbers():
    assert subtract(7, 7) == 0

def test_subtract_floats():
    assert subtract(5.5, 2.5) == 3.0

# --- Multiplication tests ---

def test_multiply():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(5, 0) == 0

def test_multiply_negative_numbers():
    assert multiply(-3, -4) == 12

def test_multiply_mixed_sign():
    assert multiply(-3, 4) == -12

def test_multiply_floats():
    assert multiply(2.5, 4) == 10.0
