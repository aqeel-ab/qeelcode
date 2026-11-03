from solutions.longest_common_prefix import longestCommonPrefix


def test_longestCommonPrefix_basic():
    assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


def test_longestCommonPrefix_no_common_prefix():
    assert longestCommonPrefix(["dog", "racecar", "car"]) == ""


def test_longestCommonPrefix_same_prefix():
    assert longestCommonPrefix(["interview", "internet", "internal"]) == "inter"


def test_longestCommonPrefix_single_word():
    assert longestCommonPrefix(["hello"]) == "hello"


def test_longestCommonPrefix_empty_list():
    assert longestCommonPrefix([]) == ""