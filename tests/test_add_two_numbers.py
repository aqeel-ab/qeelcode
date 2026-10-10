from solutions.add_two_numbers import ListNode, add_two_numbers


def create_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(node):
    values = []

    while node:
        values.append(node.val)
        node = node.next

    return values


def test_add_two_numbers_basic():
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])

    result = add_two_numbers(l1, l2)

    assert linked_list_to_list(result) == [7, 0, 8]


def test_add_two_numbers_with_zero():
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])

    result = add_two_numbers(l1, l2)

    assert linked_list_to_list(result) == [0]


def test_add_two_numbers_with_carry():
    l1 = create_linked_list([9, 9, 9])
    l2 = create_linked_list([1])

    result = add_two_numbers(l1, l2)

    assert linked_list_to_list(result) == [0, 0, 0, 1]