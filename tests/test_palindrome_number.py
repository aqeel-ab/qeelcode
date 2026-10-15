
from solutions.palindrome_number import isPalindrome


def test_positive_palindrome():
    assert isPalindrome(121) is True


def test_negative_num():
    assert isPalindrome(-121) is False


def test_number_ending_in_zero():
    assert isPalindrome(10) is False


def test_zero():
    assert isPalindrome(0) is True


def test_even_len_palindrome():
    assert isPalindrome(1221) is True


def test_non_palindrome():
    assert isPalindrome(123) is False


def test_single_digit():
    assert isPalindrome(7) is True


def test_repeated_digits():
    assert isPalindrome(11111) is True


def test_large_palindrome():
    assert isPalindrome(123454321) is True
