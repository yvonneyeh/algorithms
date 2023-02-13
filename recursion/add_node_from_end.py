"""
Given a linked list of integers and a number, k, add k to every kth node starting from the end. For example, if the list is [1 -> 2 -> 3 -> 4] and k is 3, then the result is [1 -> 5 -> 3 -> 4]. The 2 was the third value from the end, we added three to get 5. No other nodes are modified.

For a longer example, consider the list:

[1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7]
If k=3, two nodes change:

[1 -> 5 -> 3 -> 4 -> 8 -> 6 -> 7]
[execution time limit] 4 seconds (py3)

[input] linkedlist.integer head

[input] integer k

[output] linkedlist.integer
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head, k):

    dummy = ListNode(0)
    dummy.next = head

    # base case, head is null, return None

    current = head

    if not current:
        return None

    # reverse linked list

    previous = None
    original_next = None

    while current:
        original_next = current.next
        current.next = previous
        previous = current
        current = current.next

    current = previous

    order = 1

    while current:
        if order % k == 0:
            current.value += k

    while current:
        original_next = current.next
        current.next = previous
        previous = current
        current = current.next

    return previous


def recursive(head, k):

    dummy = ListNode(0)
    dummy.next = head

    # base case, head is null, return None

    current = head

    if not current:
        return None

    # reverse linked list

    previous = None
    original_next = None

    while current:
        original_next = current.next
        current.next = previous
        previous = current
        current = current.next

    current = previous

    order = 1

    def update_node_value(current, order, k):
        if not current:
            return
        if order % k == 0:
            current.value += k
        current = current.next

        update_node_value(current, order + 1, k)

    current = previous
    order = 1
    update_node_value(current, order, k)

    while current:
        original_next = current.next
        current.next = previous
        previous = current
        current = current.next

    return previous
