"""
Q. Given an unsorted linked list, find the element with the largest value.

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 ➞ 1 // returns 5
• Given a linked list: 1  // returns 1

Approach:
Call the function recursively on the next node in the list. Return the max between the current node's value and the return value from your recursive call.
"""

class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

def findMax(node: ListNode) -> int:

    if not node:
        return None

    maximum = float("-inf")

    if node.value > maximum:
        return max(maximum, findMax(node.next))

    return findMax(node)

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5, ListNode(1))))
LL2 = ListNode(7, ListNode(1, ListNode(5, ListNode(1))))
LL3 = ListNode(-1, ListNode(-3, ListNode(-5, ListNode(0, ListNode(-11)))))
print(findMax(LL1)) # 5
print(findMax(LL2)) # 7
print(findMax(LL3)) # 0
print(findMax(ListNode(1))) # 1
