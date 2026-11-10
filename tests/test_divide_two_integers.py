from solutions.divide_two_integers import divide


def test_divide_positive_numbers():
    assert divide(10, 3) == 3


def test_divide_negative_result():
    assert divide(7, -3) == -2


def test_divide_both_negative():
    assert divide(-10, -3) == 3


def test_divide_exact_result():
    assert divide(20, 5) == 4


def test_divide_zero_dividend():
    assert divide(0, 5) == 0


def test_divide_dividend_smaller_than_divisor():
    assert divide(3, 5) == 0


def test_divide_integer_overflow():
    assert divide(-(2**31), -1) == (2**31) - 1


def test_divide_minimum_integer():
    assert divide(-(2**31), 1) == -(2**31)