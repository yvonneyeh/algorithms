# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        # find middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse latter half
        backwards = None
        while slow:
            temp = slow.next
            slow.next = backwards
            backwards = slow
            slow = temp

        # compare front and back half:
        while backwards:
            if backwards.val != head.val:
                return False
            head = head.next
            backwards = backwards.next
        return True
