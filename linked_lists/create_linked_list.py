"""
A linked list is a data structure made of a chain of node objects. Each node contains a value and a pointer to the next node in the chain.

Linked lists are preferred over arrays due to their dynamic size and ease of insertion and deletion properties.

The head pointer points to the first node, and the last element of the list points to null. When the list is empty, the head pointer points to null.

"""

# A single node of a singly linked list
class Node:
    # Constructor
    def __init__(self, data, next=None):
        self.data = data  # assign data
        self.next = next  # initialize next node, default is null

# Join nodes to get a linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion method, adds a node to the linked list
    def insert(self, data):
        new_node = Node(data)

        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

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

# Creating a single node
first = Node(3)
print(first.data)

# Linked List with a single node
LL = LinkedList()
LL.head = Node(3)
print(LL.head.data)
