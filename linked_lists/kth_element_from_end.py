"""
Q. Given a linked list, return the kth element from the end of the list.
   If the k exceeds the length of the list, return -1.

Examples:
• Given a linked list: 13 ➞ 1 ➞ 5 ➞ 3 ➞ 7 ➞ 10, k: 1 // returns 10
• Given a linked list: 13 ➞ 1 ➞ 5 ➞ 3 ➞ 7 ➞ 10, k: 7 // returns -1
"""

class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

    def __repr__(self):
        print(f"{self.value} -> {self.next}")

# 2 passes
def kthFromLast_iterative(head: ListNode, k: int) -> int:

    if not head:
        return None

    current = head
    n = 0

    while current:
        current = current.next
        n += 1

    if k > n:
        return -1

    if n >= k:
        for i in range(n - k):
            head = head.next

    return head.value

# 1 pass

def kthFromLast(head: ListNode, k: int) -> int:

    current = head

    # move pointer ahead by K
    for i in range(k):
        if not current:
            return None
        current = current.next

    # iterate until current reaches end, it will be ahead by k
    while current:
        current = current.next
        head = head.next

    return head.value

# Test Cases
LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))
print(kthFromLast(LL1, 1)) # 10
print(kthFromLast(LL1, 3)) # 3
print(kthFromLast(LL1, 6)) # 13
print(kthFromLast(LL1, 7)) # -1
print(kthFromLast(None, 7)) # None


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head, n):

    if not head:
        return None

    slow = fast = head
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for i in range(1, n):
        if not fast:
            return None
        fast = fast.next

    while fast:
        if fast.next == None:
            prev.next = slow.next
        prev = slow
        slow = slow.next
        fast = fast.next

    return dummy.next
