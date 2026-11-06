class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy

    while True:
        kth = group_prev

        # Check whether k nodes are available
        for _ in range(k):
            kth = kth.next

            if not kth:
                return dummy.next

        group_next = kth.next

        # Reverse the current group
        prev = group_next
        current = group_prev.next

        while current != group_next:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # Connect the reversed group
        temp = group_prev.next
        group_prev.next = kth
        group_prev = temp

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
head = create_linked_list([1, 2, 3, 4, 5])
result = reverseKGroup(head, 2)

print_linked_list(result)