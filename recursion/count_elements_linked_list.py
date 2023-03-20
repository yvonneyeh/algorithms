"""
Q. Given an unsorted linked list, count the number of elements (iteratively or recursively).

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 // returns 3
• Given a linked list: 0 // returns 1
"""

class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

# iterative
def count(node: ListNode) -> int:

    count = 0
    current = node

    while current:
        current = current.next
        count += 1

    return count

# recursive
def count(node: ListNode) -> int:
    if not node:
        return 0

    return count(node.next) + 1

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(count(None)) # 0
print(count(LL1)) # 3
print(count(ListNode())) # 1
