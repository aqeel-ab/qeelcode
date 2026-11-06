from solutions.reverse_nodes_in_k_group import ListNode, reverseKGroup


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


def test_reverseKGroup_basic():
    head = create_linked_list([1, 2, 3, 4, 5])
    result = reverseKGroup(head, 2)

    assert linked_list_to_list(result) == [2, 1, 4, 3, 5]


def test_reverseKGroup_group_of_three():
    head = create_linked_list([1, 2, 3, 4, 5])
    result = reverseKGroup(head, 3)

    assert linked_list_to_list(result) == [3, 2, 1, 4, 5]


def test_reverseKGroup_k_equals_one():
    head = create_linked_list([1, 2, 3])
    result = reverseKGroup(head, 1)

    assert linked_list_to_list(result) == [1, 2, 3]


def test_reverseKGroup_k_equals_length():
    head = create_linked_list([1, 2, 3])
    result = reverseKGroup(head, 3)

    assert linked_list_to_list(result) == [3, 2, 1]


def test_reverseKGroup_empty_list():
    assert reverseKGroup(None, 2) is None