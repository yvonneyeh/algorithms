'''
We've been given a linked list of integer values from 0 - 2^32, and we want to delete all of the nodes that are *even* and return the list's head.

We should return the modified input linked list as our result.


EXAMPLE(S)
[3,1,3] => [3, 1, 3]
[5, 6, 9] => [5, 9]
[2, 2, 2] => [] <- edge case
[2, 7, 4, 3, 5] => [7, 3, 5]


FUNCTION SIGNATURE
function deleteEvenNodes(head) {

edge case where the list becomes empty or starts empty
    - use dummy/sentinel node that points to first element in list
    - if not head node, return None

use prev to keep track of previous node as we traverse through list
    - we want to check value mod 2 to see if it's even
        - set prev.next to node.next when when we want to remove a value
'''

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        l = []
        node = self
        while node is not None:
            l.append(node.value)
            node = node.next
        return str(l)

def delete_even_nodes(head):

    if not head:
        return None

    current = head
    prev = None

    while current:
        # print(current.value)
        # print(prev.value if prev is not None else None)
        if current.value % 2 == 0:
            # print("current is even")
            # not prev is true when prev is falsy
            # we want when prev is truthy
            if prev is not None:
                prev.next = current.next
                current = current.next
            else:
                # print("removing head")
                # print(current.value)
                head = head.next
                current = head
            continue

        prev = current
        current = current.next
        # print("---")
        # print(prev.value)
        # if current:
        #     print(current.value)
        # print()

    return head


l1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
l2 = Node(2, Node(2, Node(2, Node(2, Node(2)))))
l3 = Node(1, Node(3, Node(5, Node(7, Node(9)))))

print(delete_even_nodes(l1))
print(delete_even_nodes(l2))
print(delete_even_nodes(None))
print(delete_even_nodes(l3))
