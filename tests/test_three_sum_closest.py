from solutions.three_sum_closest import threeSumClosest


def test_threeSumClosest_basic():
    assert threeSumClosest([-1, 2, 1, -4], 1) == 2


def test_threeSumClosest_exact_target():
    assert threeSumClosest([0, 2, 1, -3], 0) == 0


def test_threeSumClosest_all_positive():
    assert threeSumClosest([1, 1, 1, 1], 0) == 3


def test_threeSumClosest_negative_target():
    assert threeSumClosest([-3, -2, -5, 3, -4], -1) == -2