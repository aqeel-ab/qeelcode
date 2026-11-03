from solutions.roman_to_integer import romanToInt


def test_romanToInt_basic():
    assert romanToInt("III") == 3


def test_romanToInt_subtractive():
    assert romanToInt("MCMXCIV") == 1994


def test_romanToInt_small_value():
    assert romanToInt("LVIII") == 58


def test_romanToInt_nine():
    assert romanToInt("IX") == 9


def test_romanToInt_single_symbol():
    assert romanToInt("M") == 1000
