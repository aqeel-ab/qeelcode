from solutions.four_sum import fourSum


def test_fourSum_basic():
    assert fourSum([1, 0, -1, 0, -2, 2], 0) == [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1],
    ]


def test_fourSum_no_solution():
    assert fourSum([1, 2, 3, 4], 100) == []


def test_fourSum_duplicates():
    assert fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]


def test_fourSum_negative_numbers():
    assert fourSum([-3, -1, 0, 2, 4, 5], 2) == [
        [-3, -1, 2, 4]
    ]