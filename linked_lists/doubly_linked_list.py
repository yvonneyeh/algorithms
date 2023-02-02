class DLLNode:
  def __init__(self, val, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev

dllHead = DLLNode(5)
x2 = DLLNode(10)
x3 = DLLNode(15)
x4 = DLLNode(22)
dllTail = DLLNode(20)

# connecting the next pointers
# None <- 5 -> 10 -> 15 -> 22 -> 20 -> None
dllHead.next = x2
x2.next = x3
x3.next = x4
x4.next = dllTail

# connecting the prev pointers
# None <- 5 <-> 10 <-> 15 <-> 22 <-> 20 -> None
dllTail.prev = x4
x4.prev = x3
x3.prev = x2
x2.prev = dllHead

print "The doubly linked list is: 5 <-> 10 <-> 15 <-> 22 <-> 20"

def printLinkedList(head):
  while head:
    print str(head.val) + " -> ",
    head = head.next
  print "None"

print "\nIterating through the list using next pointers:\n",
printLinkedList(dllHead)

def printLinkedListBackwards(tail):
  while tail:
    print str(tail.val) + " -> ",
    tail = tail.prev
  print "None"

print "\nIterating through the list using prev pointers:\n",
printLinkedListBackwards(dllTail)

###############################################################################


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Implementation for Doubly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with 'dummy' head and tail nodes which makes
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    def insertEnd(self, val):
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode

    # Remove first node after dummy head (assume it exists)
    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    # Remove last node before dummy tail (assume it exists)
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def print(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, " -> ")
            curr = curr.next
        print()
