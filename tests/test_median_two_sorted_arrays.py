from solutions.median_two_sorted_arrays import findMedianSortedArray


def test_odd_total_len():
    assert findMedianSortedArray([1, 3], [2]) == 2.0


def test_even_total_len():
    assert findMedianSortedArray([1, 2], [3, 4]) == 2.5


def test_different_array_lengths():
    assert findMedianSortedArray([1, 4, 7], [2, 3, 8]) == 3.5


def test_one_empty_array():
    assert findMedianSortedArray([], [1, 2, 3, 4, 5]) == 3.0


def test_first_array_larger():
    assert findMedianSortedArray([1, 3, 5, 7], [2, 4]) == 3.5


def test_negative_numbers():
    assert findMedianSortedArray([-5, -3], [-4, -2]) == -3.5


def test_duplicate_values():
    assert findMedianSortedArray([1, 2, 2], [2, 3, 4]) == 2.0
