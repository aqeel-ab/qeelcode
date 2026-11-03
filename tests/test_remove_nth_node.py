from solutions.remove_nth_node import ListNode, removeNthFromEnd


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


def test_remove_middle_node():
    head = build_list([1, 2, 3, 4, 5])
    assert to_list(removeNthFromEnd(head, 2)) == [1, 2, 3, 5]


def test_remove_first_node():
    head = build_list([1, 2, 3])
    assert to_list(removeNthFromEnd(head, 3)) == [2, 3]


def test_remove_last_node():
    head = build_list([1, 2, 3])
    assert to_list(removeNthFromEnd(head, 1)) == [1, 2]


def test_remove_only_node():
    head = build_list([1])
    assert removeNthFromEnd(head, 1) is None