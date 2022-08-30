# Merge Two Sorted Linked Lists
"""
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create dummy node (starter) as to not insert into empty linked list
        starter = tail = ListNode(0)


        while (l1 and l2): # l1 != None and l2 != None
            if (l1.val < l2.val):
                tail.next = l1
                l1 = l1.next
            elif (l1.val >= l2.val):
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        # for cases where one list is empty, or add whatever is left
        tail.next = l1 or l2

        return starter.next # returns everything newly added, excluding dummy node

# Time: O(m+n) - length of 2 lists
# Space: O(1)
