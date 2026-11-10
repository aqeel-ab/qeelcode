from solutions.substring_with_concatenation_of_all_words import findSubstring


def test_findSubstring_basic():
    assert findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]


def test_findSubstring_multiple_matches():
    result = findSubstring(
        "barfoofoobarthefoobarman",
        ["bar", "foo", "the"]
    )

    assert result == [6, 9, 12]


def test_findSubstring_repeated_words():
    assert findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]) == [8]


def test_findSubstring_no_match():
    assert findSubstring("abcdef", ["foo", "bar"]) == []


def test_findSubstring_word_longer_than_string():
    assert findSubstring("hi", ["hello"]) == []


def test_findSubstring_empty_words():
    assert findSubstring("barfoo", []) == []


def test_findSubstring_single_word():
    assert findSubstring("hello", ["ll"]) == [2]


def test_findSubstring_overlapping_matches():
    assert findSubstring("aaaaaa", ["aa", "aa"]) == [0, 1, 2]