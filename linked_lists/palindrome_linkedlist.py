# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        current = head
        arr = []

        while current:
            arr.append(current.val)
            current = current.next

        l = 0
        r = len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1

        return True

        # mid = len(arr) // 2

        # print(arr[:mid], arr[mid::-1])

        # return arr[:mid] == arr[mid:]


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
