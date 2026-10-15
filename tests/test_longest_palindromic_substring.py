from solutions.longest_palindromic_substring import longestPalindrome

def test_odd_palindrome():
    assert longestPalindrome("babad") in ("bab", "aba")

def test_even_palindrome():
    assert longestPalindrome("cbbd") == "bb"

def test_single_character():
    assert longestPalindrome("a") == "a"

def test_two_different_characters():
    assert longestPalindrome("ac") in ("a", "c")

def test_empty_string():
    assert longestPalindrome("") == ""

def test_entire_string_is_palindrome():
    assert longestPalindrome("racecar") == "racecar"

def test_all_same_characters():
    assert longestPalindrome("aaaa") == "aaaa"
