from solutions.merge_k_sorted_lists import (
    ListNode,
    mergeKLists
)


def create_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(node):
    result = []

    while node:
        result.append(node.val)
        node = node.next

    return result


def test_mergeKLists_basic():
    lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]

    result = mergeKLists(lists)

    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_mergeKLists_empty_lists():
    assert mergeKLists([]) is None


def test_mergeKLists_all_empty():
    assert mergeKLists([None, None]) is None


def test_mergeKLists_single_list():
    lists = [create_linked_list([1, 2, 3])]

    result = mergeKLists(lists)

    assert linked_list_to_list(result) == [1, 2, 3]


def test_mergeKLists_duplicate_values():
    lists = [
        create_linked_list([1, 1]),
        create_linked_list([1, 1])
    ]

    result = mergeKLists(lists)

    assert linked_list_to_list(result) == [1, 1, 1, 1]