from solutions.valid_parentheses import isValid


def test_valid_parentheses():
    assert isValid("()[]{}") is True


def test_mismatched_brackets():
    assert isValid("(]") is False


def test_wrong_nesting():
    assert isValid("([)]") is False


def test_unclosed_bracket():
    assert isValid("(((") is False


def test_empty_string():
    assert isValid("") is True