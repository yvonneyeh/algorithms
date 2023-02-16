"""Q. Given two linked lists of different length, sum elements' value at the same position.

Example:
Input: LL1: 1->2->5, LL2: 3->4
Output: 4->6->5
[execution time limit] 4 seconds (py3)

[input] linkedlist.integer head1

head of the list1

[input] linkedlist.integer head2

head of the list2

[output] linkedlist.integer

head of the summed list"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head1, head2):

    if not head1 or not head2:
        return None

    dummy = ListNode(0)
    dummy.next = head1

    while head1 and head2:
        head1.value += head2.value
        head1 = head1.next
        head2 = head2.next

    return dummy.next

"""
Case 1:
Input:
head1: []
head2: [1]
Output:
[]
Expected Output:
[1]


Case 2:
Input:
head1: [2, 4]
head2: [1, 2, 3]
Output:
[3, 6]
Expected Output:
[3, 6, 3]
"""

"""
Q. Given an unsorted linked list with unique values, insert an element before the target element

If target cannot be found in the list, do nothing.
Example:

Given a linked list: 3 -> -1 -> 2 -> 5, element (to be inserted): 0, target: 2
// returns: 3 -> -1 -> 0 -> 2 -> 5
[execution time limit] 4 seconds (py3)

[input] linkedlist.integer head

head of the list

[input] integer target

vale of the target node

[input] integer value

value of the node to be inserted before the target node

[output] linkedlist.integer

head of the updated list
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head, target, value):

    if not head or not target or not value:
        return None

    dummy = ListNode(0)
    dummy.next = current = head
    previous = dummy

    while current:
        if current.value == target:
            new = ListNode(value)
            new.next = current
            previous.next = new
        previous = current
        current = current.next

    return dummy.next

"""
Input:
head: [3, -1, 2, 5]
target: 2
value: 0
Output:
[]
Expected Output:
[3, -1, 0, 2, 5]
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

    previous = head.value
    current = head
    while current:
        if current.value < previous:
            return False
        previous = current.value
        current = current.next

    return True


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head1, head2):

    if not head1 or not head2:
        return None

    dummy = ListNode(0)
    dummy.next = head1

    h1_len = 0
    h2_len = 0

    while head1:
        h1_len += 1
        head1 = head1.next

    while head1:
        h1_len += 1
        head1 = head1.next

    if h1_len > h2_len:
        while head1:
            head1.value += head2.value
            head1 = head1.next
            head2 = head2.next


    while head1 and head2:
        head1.value += head2.value
        head1 = head1.next
        head2 = head2.next

    return head1.next


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):

    if not head:
        return None

    slow = fast = head

    while fast and fast.next.next.next:
        slow = slow.next
        fast = fast.next.next.next

    return slow.value


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head, k):

    if not head:
        return None

    order = 1
    result = ListNode(-1)

    while head:
        order += 1
        if order == k:
            result = head
        head = head.next

    return result


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head, target, value):

    if not head or not target or not value:
        return None

    dummy = ListNode(0)
    dummy.next = current = head
    previous = dummy

    while current:
        if current.value == target:
            original_next = current.next
            current = ListNode(value)
            previous.next = current
            current.next = original_next
        previous = current
        current = current.next

    return dummy.next


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

# WIP

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



"""Q. Given an array, create a linked list with its values in the order they appear in the array."""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(array):

    if not array:
        return None

    sorted(array)

    start = current = ListNode(0)

    for value in array:
        current.next = ListNode(value)
        current = current.next

    return start.next

"""Q. Given a linked list, insert a node with the value 0 after each existing node. This should double the length of the original list and every other value should be a 0."""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):

    if not head:
        return None

    current = head

    while current:
        original_next = current.next
        new = ListNode(0)
        current.next = new
        new.next = original_next
        current = current.next.next

    return head

"""Q. Given a target integer and count integer, create a linked list of length count, where each node has the value target."""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(target, count):

    if not count:
        return None

    start = current = ListNode(0)

    for i in range(count):
        current.next = ListNode(target)
        current = current.next

    return start.next

"""Q. Given a linked list of positive integers, find the first element that occurs at least k number of times."""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head, k):

    if not head:
        return -1

    count = {}

    while head:
        count[head.value] = count.get(head.value, 0) + 1
        if count[head.value] == k:
            return head.value
        head = head.next

    return -1

"""Q. Given a linked list, limit the number of repetitions to k. Iterate through the linked list, keeping track of how many times the value has been repeated. Once a value has been repeated k target number of times, remove any future instances of that node."""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head, k):

    if not head or not k:
        return None

    count = {}
    current = head
    prev = None

    while current:
        count[current.value] = count.get(current.value, 0) + 1
        if count[current.value] > k:
            prev.next = current.next
        else:
            prev = current
        current = current.next

    return head


"""Q. Given a linked list, remove all nodes with an odd value from the list."""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):

    if not head:
        return None

    current = head
    prev = None

    while current:
        if current.value % 2 == 1:
            if prev is not None:
                prev.next = current.next
                current = current.next
            else:
                head = head.next
                current = head
            continue
        prev = current
        current = current.next

    return head


"""Remove N from end"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head, n):

    if not head:
        return None

    current = head
    prev = None

    while current:
        original_next = current.next
        current.next = prev
        prev = current
        current = current.next

    current = prev
    prev = None

    for i in range(1, n):
        if i == n:
            prev.next = current.next
            break
        prev = current
        current = current.next


    current = head
    prev = None

    while current:
        original_next = current.next
        current.next = prev
        prev = current
        current = current.next

    return head


"""
Given a linked list of integers, return the sum of every other value, starting with the second.
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):

    if not head:
        return 0

    result = 0
    current = head
    count = 1

    # while current.next and current.next.next:
    #     result += current.next.value
    #     current = current.next.next

    while current:
        if count % 2 == 0:
            result += current.value
        count += 1
        current = current.next

    return result

"""
Given a linked list of integers, return the sum of every other value, starting with the second.

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer head

[output] integer
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):

    if not head:
        return 0

    result = 0
    current = head

    while current.next and current.next.next:
        result += current.next.value
        current = current.next.next

    return result
