from solutions.swap_nodes_in_pairs import ListNode, swapPairs


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


def test_swapPairs_basic():
    head = create_linked_list([1, 2, 3, 4])
    result = swapPairs(head)

    assert linked_list_to_list(result) == [2, 1, 4, 3]


def test_swapPairs_odd_length():
    head = create_linked_list([1, 2, 3])
    result = swapPairs(head)

    assert linked_list_to_list(result) == [2, 1, 3]


def test_swapPairs_empty_list():
    assert swapPairs(None) is None


def test_swapPairs_single_node():
    head = create_linked_list([1])
    result = swapPairs(head)

    assert linked_list_to_list(result) == [1]


def test_swapPairs_two_nodes():
    head = create_linked_list([1, 2])
    result = swapPairs(head)

    assert linked_list_to_list(result) == [2, 1]