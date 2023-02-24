# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

"""
Approach: The recursive solution can be formed, given the linked lists are sorted.

Compare the head of both linked lists.
Find the smaller node among the two head nodes. The current element will be the smaller node among two head nodes.
The rest elements of both lists will appear after that.
Now run a recursive function with parameters, the next node of the smaller element, and the other head.
The recursive function will return the next smaller element linked with rest of the sorted element. Now point the next of current element to that, i.e curr_ele->next=recursivefunction()
Handle some corner cases.
If both the heads are NULL return null.
If one head is null return the other.
"""

def merge(list1, list2):

    if not list1:
        return list2

    if not list2:
        return list1

    if list1.value < list2.value:
        list1.next = merge(list1.next, list2)
        return list1

    else: # list2.value < list1.value
        list2.next = merge(list1, list2.next)
        return list2
