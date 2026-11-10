from solutions.find_the_index_of_the_first_occurrence import strStr


def test_strStr_basic():
    assert strStr("sadbutsad", "sad") == 0


def test_strStr_occurrence_in_middle():
    assert strStr("hello", "ll") == 2


def test_strStr_needle_not_found():
    assert strStr("leetcode", "leeto") == -1


def test_strStr_needle_same_as_haystack():
    assert strStr("abc", "abc") == 0


def test_strStr_empty_needle():
    assert strStr("abc", "") == 0


def test_strStr_needle_longer_than_haystack():
    assert strStr("hi", "hello") == -1