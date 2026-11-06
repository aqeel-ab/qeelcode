from solutions.generate_parentheses import generateParenthesis


def test_generateParenthesis_basic():
    assert generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]


def test_generateParenthesis_one_pair():
    assert generateParenthesis(1) == ["()"]


def test_generateParenthesis_two_pairs():
    assert generateParenthesis(2) == ["(())", "()()"]


def test_generateParenthesis_four_pairs():
    assert len(generateParenthesis(4)) == 14


def test_generateParenthesis_zero_pairs():
    assert generateParenthesis(0) == [""]