from solutions.remove_element import removeElement


def test_removeElement_basic():
    nums = [3, 2, 2, 3]

    k = removeElement(nums, 3)

    assert k == 2
    assert sorted(nums[:k]) == [2, 2]


def test_removeElement_multiple_occurrences():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]

    k = removeElement(nums, 2)

    assert k == 5
    assert sorted(nums[:k]) == [0, 0, 1, 3, 4]


def test_removeElement_no_occurrences():
    nums = [1, 2, 3, 4]

    k = removeElement(nums, 5)

    assert k == 4
    assert sorted(nums[:k]) == [1, 2, 3, 4]


def test_removeElement_all_occurrences():
    nums = [2, 2, 2, 2]

    k = removeElement(nums, 2)

    assert k == 0
    assert nums[:k] == []


def test_removeElement_empty_array():
    nums = []

    k = removeElement(nums, 3)

    assert k == 0
    assert nums[:k] == []