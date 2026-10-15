from solutions.zigzag_conversion import convert

def test_three_rows():
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

def test_four_rows():
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

def test_five_chars_three_rows():
    assert convert("ABCDE", 3) == "AEBDC"


def test_one_row():
    assert convert("ABCDE", 1) == "ABCDE"


def test_num_rows_greater_than_string_len():
    assert convert("AB", 5) == "AB"


def test_single_character():
    assert convert("A", 1) == "A"


def test_empty_string():
    assert convert("", 3) == ""


def test_two_rows():
    assert convert("ABCDE", 2) == "ACEBD"