# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):

    if not head:
        return None

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head

    while current and current.next:
        # save node pointers
        next_pair = current.next.next
        second = current.next
        # swap
        second.next = current
        current.next = next_pair
        prev.next = second
        # update pointers
        prev = current
        current = next_pair

    return dummy.next
