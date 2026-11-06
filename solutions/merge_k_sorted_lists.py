import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: list[ListNode]) -> ListNode:
    min_heap = []
    counter = 0

    for node in lists:
        if node:
            heapq.heappush(min_heap, (node.val, counter, node))
            counter += 1

    dummy = ListNode()
    current = dummy

    while min_heap:
        val, _, node = heapq.heappop(min_heap)

        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(min_heap, (node.next.val, counter, node.next))
            counter += 1

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
lists = [
    create_linked_list([1, 4, 5]),
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6])
]

merged = mergeKLists(lists)
print_linked_list(merged)