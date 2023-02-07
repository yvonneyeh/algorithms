# Linked List

Linked lists (LL), or singly linked lists, are a data structure created from a chain of nodes where each node is an object that contains two fields: a data value and a pointer to the next node. Similar to other objects, the Node class definition defines these two fields. The chaining that creates a LL occurs when the 'next' pointer references another Node object. This chaining of nodes creates a recursive data structure known as a linked list.

## Worst Case
- space	O(n)
- prepend	O(1)
- append	O(1)
- lookup	O(n)
- insert	O(n)
- delete	O(n)

A linked list organizes items sequentially, with each item storing a pointer to the next one.

Picture a linked list like a chain of paperclips linked together. It's quick to add another paperclip to the top or bottom. It's even quick to insert one in the middle—just disconnect the chain at the middle link, add the new paperclip, then reconnect the other half.

An item in a linked list is called a _node_. The first node is called the _head_. The last node is called the _tail_.

> Confusingly, sometimes people use the word tail to refer to "the whole rest of the list after the head."

A linked list with 3 nodes. The first node is labelled "head" and the last node is labelled "tail."

Unlike an array, consecutive items in a linked list are not necessarily next to each other in memory.

## Strengths:
- Fast operations on the ends. Adding elements at either end of a linked list is O(1). Removing the first element is also O(1).
- Flexible size. There's no need to specify how many elements you're going to store ahead of time. You can keep adding elements as long as there's enough space on the machine.

## Weaknesses:
- Costly lookups. To access or edit an item in a linked list, you have to take O(i) time to walk from the head of the list to the iith item.

##Uses:
- Stacks and queues only need fast operations on the ends, so linked lists are ideal.

### In Python 3.6
Most languages (including Python 3.6) don't provide a linked list implementation. Assuming we've already implemented our own, here's how we'd construct the linked list above:

  a = LinkedListNode(5)
b = LinkedListNode(1)
c = LinkedListNode(9)

a.next = b
b.next = c

# Doubly Linked Lists
In a basic linked list, each item stores a single pointer to the next element.

In a doubly linked list, items have pointers to the next and the previous nodes.

A doubly-linked list with 3 nodes. The first node has value 5 with a "next" arrow pointing ahead to the second node and a "previous" arrow pointing back to "None." The second node has value 1 with a "next" arrow pointing ahead to the third node and a "previous" arrow pointing back to the first node. The third node has value 9 with a "next" arrow pointing ahead to "None" and a "previous" arrow pointing back to the second node.
Doubly linked lists allow us to traverse our list backwards. In a singly linked list, if you just had a pointer to a node in the middle of a list, there would be no way to know what nodes came before it. Not a problem in a doubly linked list.

## Not cache-friendly
Most computers have caching systems that make reading from sequential addresses in memory faster than reading from scattered addresses.

Array items are always located right next to each other in computer memory, but linked list nodes can be scattered all over.

So iterating through a linked list is usually quite a bit slower than iterating through the items in an array, even though they're both theoretically O(n)O(n) time.


```
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head

    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, " -> ", end="")
            curr = curr.next
        print()

```
