# Given a linked list, delete the middle node. If the list is even length, delete the node at the start of the second half of the list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value  # assign value
        self.next = next  # initialize next node, default is null

class LinkedList:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:


class LinkedList:
    def __init__(self):
        self.head = None

    def delete(self, key):
        # Store head node
        temp = self.head

        # If head node holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if(temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None
