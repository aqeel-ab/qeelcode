
from solutions.regular_expression_matching import isMatch


def test_no_match():
    assert isMatch("aa", "a") is False


def test_star_matches_repeated_char():
    assert isMatch("aa", "a*") is True


def test_dot_matches_any_char():
    assert isMatch("ab", ".*") is True


def test_star_matches_zero_occurrences():
    assert isMatch("aab", "c*a*b") is True


def test_complex_pattern_no_match():
    assert isMatch("mississippi", "mis*is*p*.") is False


def test_empty_str_and_empty_pattern():
    assert isMatch("", "") is True


def test_empty_str_with_star_pattern():
    assert isMatch("", "a*") is True


def test_single_char_match():
    assert isMatch("a", "a") is True


def test_dot_matches_single_char():
    assert isMatch("a", ".") is True


def test_repeated_pattern():
    assert isMatch("aaa", "a*a") is True


def test_multiple_stars():
    assert isMatch("ab", ".*c") is False


def test_star_matches_zero_occurrences():
    assert isMatch("ab", "a*b") is True
