"""Q. Given a linked list, limit the number of repetitions to k. Iterate through the linked list, keeping track of how many times the value has been repeated. Once a value has been repeated k target number of times, remove any future instances of that node.

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer head

[input] integer k

[output] linkedlist.integer

head of the list"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head, k):

    dummy = ListNode(0)
    item_count = {}
    prev = dummy
    current = head
    while current:
        item_count[current.value] = item_count.get(current.value, 0) + 1
        if item_count[current.value] > k:
            prev.next = current.next
        else:
            prev = current
            current = current.next

    print(item_count)
    print(dummy.next)

    return dummy.next

"""
Q. Given a linked list of positive integers, remove only odd numbers at odd positions. The first position of the list is 1.

Example:
Input: [1, 2, 3, 7, 5, 2]
Output: [2, 7, 2]

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer head

[output] linkedlist.integer
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):

    dummy = ListNode(0)
    prev = dummy
    current = head
    odd = True

    while current:
        print(odd, current.value, current.value % 2)
        if current.value % 2 == 1 and odd:
            print("yes")
            prev.next = current.next
        current = current.next
        odd = not odd

    return dummy.next

"""
Q. Given two linked lists of equal length, merge them into one by taking the minimum value at the each element.

Example:
Inputs: [1, 2, 3, 4, 5] and [5, 4, 3, 2, 1]
Output:[1, 2, 3, 2, 1] // at the first element, 1 is smaller than 5. Thus, take 1 as the first element of the merged list.
[execution time limit] 4 seconds (py3)

[input] linkedlist.integer head1

head of the first list

[input] linkedlist.integer head2

head of the second list

[output] linkedlist.integer

head of the merged list

"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head1, head2):

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

"""
Q. Given a linked list, find the first occurring pair from the head with the biggest difference.

Example:
Input: [1, 2, 3, 10, 4, 11]
Output: [3, 10] // difference of 7; notice [4, 11] also differs by 7

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer head

[output] linkedlist.integer

"""
def solution(head):

    max_diff = float("-inf")

    seen = {}


"""
Q. Given an integer k, create a linked list representing the first k values of the Fibonacci sequence.

For example, given k = 1, return this list:
1

Given k = 6, return this list:
1 -> 1 -> 2 -> 3 -> 5 -> 8

Return
the head of new list

[execution time limit] 4 seconds (py3)

[input] integer k

The number of fibonacci elements to include

[output] linkedlist.integer

The head of the new list
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(k):

    if k < 1:
        return None

    prev = None
    current = ListNode(1)
    a = 1
    b = 1
    while k > 0:
        current_value = prev.value

    return head

"""
Q. Given a linked list, determine if it is monotonically increasing. Monotonically increasing means always increasing or remaining constant.

Examples:

Given a linked list: 1 -> 1 -> 2 -> 5 // returns True
Given a linked list: -1 -> -5 -> 3 -> -100, // returns False
[execution time limit] 4 seconds (py3)

[input] linkedlist.integer head

head of the list

[output] boolean
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):

    if not head:
        return False

    last_value = head.value
    current = head
    while current:
        if current.value < last_value:
            return False
        last_value = current.value
        current = current.next

    return True
