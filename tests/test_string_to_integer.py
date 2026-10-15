
from solutions.string_to_integer import myAtoi


def test_positive_integer():
    assert myAtoi("42") == 42


def test_negative_integer():
    assert myAtoi(" -042") == -42


def test_stops_at_non_digit():
    assert myAtoi("1337c0d3") == 1337


def test_string_starts_with_words():
    assert myAtoi("words and 987") == 0


def test_negative_overflow():
    assert myAtoi("-91283472332") == -2147483648


def test_positive_overflow():
    assert myAtoi("91283472332") == 2147483647


def test_positive_sign():
    assert myAtoi("+17") == 17


def test_empty_string():
    assert myAtoi("") == 0


def test_only_whitespace():
    assert myAtoi("   ") == 0


def test_sign_without_digits():
    assert myAtoi("+") == 0


def test_leading_zeros():
    assert myAtoi("000123") == 123


def test_decimal_stops_at_dot():
    assert myAtoi("3.14") == 3
