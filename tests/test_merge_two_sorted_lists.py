from solutions.merge_two_sorted_lists import ListNode, mergeTwoLists


def build_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def to_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


def test_merge_two_lists():
    list1 = build_list([1, 2, 4])
    list2 = build_list([1, 3, 4])

    assert to_list(mergeTwoLists(list1, list2)) == [1, 1, 2, 3, 4, 4]


def test_one_empty_list():
    list1 = build_list([])
    list2 = build_list([0])

    assert to_list(mergeTwoLists(list1, list2)) == [0]


def test_both_empty():
    assert mergeTwoLists(None, None) is None


def test_non_overlapping_values():
    list1 = build_list([1, 2, 3])
    list2 = build_list([4, 5, 6])

    assert to_list(mergeTwoLists(list1, list2)) == [1, 2, 3, 4, 5, 6]