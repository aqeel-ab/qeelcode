from solutions.next_permutation import nextPermutation


def test_nextPermutation_basic():
    nums = [1, 2, 3]

    nextPermutation(nums)

    assert nums == [1, 3, 2]


def test_nextPermutation_descending_order():
    nums = [3, 2, 1]

    nextPermutation(nums)

    assert nums == [1, 2, 3]


def test_nextPermutation_with_duplicates():
    nums = [1, 1, 5]

    nextPermutation(nums)

    assert nums == [1, 5, 1]


def test_nextPermutation_multiple_elements():
    nums = [1, 2, 3, 6, 5, 4]

    nextPermutation(nums)

    assert nums == [1, 2, 4, 3, 5, 6]


def test_nextPermutation_two_elements():
    nums = [1, 2]

    nextPermutation(nums)

    assert nums == [2, 1]


def test_nextPermutation_single_element():
    nums = [1]

    nextPermutation(nums)

    assert nums == [1]


def test_nextPermutation_empty_array():
    nums = []

    nextPermutation(nums)

    assert nums == []