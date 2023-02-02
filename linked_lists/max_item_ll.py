"""
Q. Given an unsorted linked list, find the element with the largest value.

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 ➞ 1 // returns 5
• Given a linked list: 1  // returns 1
"""

class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

def findMax(node: ListNode) -> int:
    max_value = float('-inf')
    current = node
    while current:
        if current.value > max_value:
            max_value = current.value
        current = current.next

    return max_value

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5, ListNode(1))))
LL2 = ListNode(7, ListNode(1, ListNode(5, ListNode(1))))
LL3 = ListNode(-1, ListNode(-3, ListNode(-5, ListNode(0, ListNode(-11)))))
print(findMax(LL1)) # 5
print(findMax(LL2)) # 7
print(findMax(LL3)) # 0
print(findMax(ListNode(1))) # 1
