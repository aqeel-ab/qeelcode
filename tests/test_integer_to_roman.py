from solutions.integer_to_roman import intToRoman


def test_int_to_roman():
    assert intToRoman(3) == "III"
    assert intToRoman(58) == "LVIII"
    assert intToRoman(1994) == "MCMXCIV"
    assert intToRoman(3749) == "MMMDCCXLIX"