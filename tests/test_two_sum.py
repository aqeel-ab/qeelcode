from solutions.two_sum import two_sum

def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_different_positions():
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_two_sum_same_value():
    assert two_sum([3, 3], 6) == [0, 1]