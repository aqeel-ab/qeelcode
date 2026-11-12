from solutions.longest_valid_parentheses import longestValidParentheses


def test_longestValidParentheses_basic():
    assert longestValidParentheses(")()())") == 4


def test_longestValidParentheses_all_valid():
    assert longestValidParentheses("()()") == 4


def test_longestValidParentheses_nested():
    assert longestValidParentheses("((()))") == 6


def test_longestValidParentheses_no_valid_parentheses():
    assert longestValidParentheses("(((") == 0


def test_longestValidParentheses_empty_string():
    assert longestValidParentheses("") == 0


def test_longestValidParentheses_separated_valid_substrings():
    assert longestValidParentheses("()(()") == 2


def test_longestValidParentheses_multiple_groups():
    assert longestValidParentheses("()(())") == 6


def test_longestValidParentheses_single_pair():
    assert longestValidParentheses("()") == 2