'''
Given the head node of a singly linked list, find nodes where they have already appeared (k) or more times.

Return the head node of the new linked list, after deleting/removing the nodes.

If a node appears more than once in a list, only the nodes that are `kth` or higher must be deleted. You can still retain the nodes leading up to the `kth` occurrence.


EXAMPLE(S)
4 -> 3 -> 4 -> 1 -> 5, k = 2 should return 4 -> 3 -> 1 -> 5

1 -> 1 -> 2, k = 2 should return 1 -> 2

1 -> 2 -> 3, k = 3 should return 1 -> 2 -> 3


FUNCTION SIGNATURE
def removeKAppearingNodes(head, k)


Edge cases:
k = 1 -> return empty linked list
k = 0 -> return same list (no changes)
k >= 0 (assume no negative Ks)
empty list -> return empty list


Brainstorm:
+ hashmap keys node values -> freq
+ keeps track of previous node & current node
+ when add the freq check if the value >= k
-> if so we delete current node, update previous with curr.next

Time O(n) n being length of LL
Space O(n)

'''

from typing import List


class Node():
    def __init__(self, val, next=None):
        self.val= val
        self.next = next

    def __repr__(self) -> str:
        return f'{self.val} -> {str(self.next)}'

def removeKAppearingNodes(head, k):
    if head == None or k == 0: return head

    dummy = Node(val = None, next = head)
    previous = dummy
    current = head
    freq = {}

    while current:
        freq[current.val] = freq.get(current.val, 0) + 1

        if freq[current.val] >= k:
            previous.next = current.next
        else:
            previous = current

        current = current.next

    return dummy.next

# 4 -> 3 -> 4 -> 1 -> 5, k = 2
# None -> 4 -> 3 -> 4 -> 1 -> 5
# freq = {4: 1}
# freq = {4:2, 3:1}
l1 = Node(4, Node(3, Node( 4, Node(1, Node(5)))))
k = 2
result = Node(4, Node(3, Node(1, Node(5))))
print(l1)
print(result)
print(removeKAppearingNodes(l1, k))
