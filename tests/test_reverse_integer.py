
from solutions.reverse_integer import reverse


def test_positive_int():
    assert reverse(123) == 321


def test_negative_int():
    assert reverse(-123) == -321


def test_trailing_zero():
    assert reverse(120) == 21


def test_zero():
    assert reverse(0) == 0


def test_overflow():
    assert reverse(1534236469) == 0


def test_single_digit():
    assert reverse(7) == 7


def test_negative_overflow():
    assert reverse(-1563847412) == 0


def test_num_with_repeated_digit():
    assert reverse(1122) == 2211
