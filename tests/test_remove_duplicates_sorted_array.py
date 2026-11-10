from solutions.remove_duplicates_sorted_array import removeDuplicates


def test_removeDuplicates_basic():
    nums = [1, 1, 2]

    k = removeDuplicates(nums)

    assert k == 2
    assert nums[:k] == [1, 2]


def test_removeDuplicates_multiple_duplicates():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    k = removeDuplicates(nums)

    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]


def test_removeDuplicates_no_duplicates():
    nums = [1, 2, 3, 4, 5]

    k = removeDuplicates(nums)

    assert k == 5
    assert nums[:k] == [1, 2, 3, 4, 5]


def test_removeDuplicates_empty_array():
    nums = []

    k = removeDuplicates(nums)

    assert k == 0
    assert nums[:k] == []


def test_removeDuplicates_single_element():
    nums = [1]

    k = removeDuplicates(nums)

    assert k == 1
    assert nums[:k] == [1]