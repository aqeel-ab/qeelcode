from solutions.three_sum import threeSum


def test_example():
    assert threeSum([-1, 0, 1, 2, -1, -4]) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]


def test_no_triplets():
    assert threeSum([1, 2, -2, -1]) == []


def test_all_zeros():
    assert threeSum([0, 0, 0, 0]) == [[0, 0, 0]]


def test_duplicate_triplets_are_removed():
    assert threeSum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]