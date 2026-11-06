from solutions.letter_combinations import letterCombinations


def test_example():
    assert letterCombinations("23") == [
        "ad", "ae", "af",
        "bd", "be", "bf",
        "cd", "ce", "cf",
    ]


def test_empty_input():
    assert letterCombinations("") == []


def test_single_digit():
    assert letterCombinations("2") == ["a", "b", "c"]


def test_digit_with_four_letters():
    assert letterCombinations("7") == ["p", "q", "r", "s"]