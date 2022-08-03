"""
A linked list is a data structure made of a chain of node objects. Each node contains a value and a pointer to the next node in the chain.

Linked lists are preferred over arrays due to their dynamic size and ease of insertion and deletion properties.

The head pointer points to the first node, and the last element of the list points to null. When the list is empty, the head pointer points to null.

"""

# A single node of a singly linked list
class Node:
    # Constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

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


# Creating a single node
first = Node(3)
print(first.data)

# Linked List with a single node
LL = LinkedList()
LL.head = Node(3)
print(LL.head.data)
