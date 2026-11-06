class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        first = current.next
        second = first.next

        first.next = second.next
        second.next = first
        current.next = second

        current = first

    return dummy.next


# Helper function for manual testing
def create_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_linked_list(node):
    result = []

    while node:
        result.append(node.val)
        node = node.next

    print(result)


# Manual test
head = create_linked_list([1, 2, 3, 4])
result = swapPairs(head)

print_linked_list(result)