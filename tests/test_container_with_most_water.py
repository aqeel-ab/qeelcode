from solutions.container_with_most_water import maxArea


def test_example():
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_two_heights():
    assert maxArea([1, 1]) == 1


def test_decreasing_heights():
    assert maxArea([4, 3, 2, 1, 4]) == 16


def test_short_container():
    assert maxArea([1, 2, 1]) == 2