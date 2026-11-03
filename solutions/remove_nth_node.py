class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Move fast n + 1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the target node
    slow.next = slow.next.next

    return dummy.next


def print_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)


# Manual test: remove the 2nd node from the end
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = removeNthFromEnd(head, 2)
print_list(result)  # Expected: [1, 2, 3, 5]