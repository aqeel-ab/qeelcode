from solutions.longest_substring import lenLongestSubstr

def test_lenLongestSubstr_basic():
    assert lenLongestSubstr("abcabcbb") == 3

def test_lenLongestSubstr_all_same():
    assert lenLongestSubstr("aaaa") == 1

def test_lenLongestSubstr_empty():
    assert lenLongestSubstr("") == 0

def test_lenLongestSubstr_middle_duplicate():
    assert lenLongestSubstr("pwwkew") == 3

def test_lenLongestSubstr_unique():
    assert lenLongestSubstr("abcdef") == 6