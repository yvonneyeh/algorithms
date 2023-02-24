'''
Given a linked list, delete K nodes after the middle.

If N is the length of the list, the middle node is [N / 2] using zero-based indexing.

Return the head of the modified list.


EXAMPLE(S)
1 -> 2 -> 3 -> 4, k = 2 should return 1 -> 2

1 -> 2 -> 3 -> 4, k = 1 should return 1 -> 2 -> 4

1, k = 0 should return 1

2 -> 9 -> 4 -> 1 -> 7, k = 3 should return 2 -> 9 -> 4

2 -> 9 -> 4 -> 1 -> 7, k = 1 should return 2 -> 9 -> 4 -> 7

EDGE CASES:
No LL -> return None
K must be >= 0

APPROACH:
- find midpoint of LL using slow/fast pointer
- to remove nodes: move .next pointer to .next.next
- decrement k until k == 0, then we stop deleting nodes
- return head of LL

FUNCTION SIGNATURE
function removeKAfterMiddle(head, k)
'''

# slow/fast, tortoise/hare pointer algorithm
# 2 -> 9 -> 4 -> 1 -> 7 -> None
        # slow
                #   fast

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        l = []
        node = self
        while node:
            l.append(node.value)
            node = node.next
        return str(l)


def find_midpoint_of_linked_list(head):

    if not head:
        return None

    slow = fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def remove_k_after_middle(head, k):

    if not head:
        return None

    mid = find_midpoint_of_linked_list(head)

    for i in range(k):
        if not mid.next:
            return head
        else:
            mid.next = mid.next.next

    return head


list1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
list2 = Node(1, Node(2, Node(3, Node(4))))
list3 = Node(1, Node(2, Node(3, Node(4))))
list4 = Node(2, Node(9, Node(4, Node(1, Node(7)))))
list5 = Node(2, Node(9, Node(4, Node(1, Node(7)))))

# print(find_midpoint_of_linked_list(list1)) #3
# print(find_midpoint_of_linked_list(list2)) #3

print(remove_k_after_middle(list2, 2)) # 1 -> 2
print(remove_k_after_middle(list3, 1)) # 1 -> 2 -> 4
print(remove_k_after_middle(list4, 3)) # 2 -> 9 -> 4
print(remove_k_after_middle(list5, 1)) # 2 -> 9 -> 4 -> 7
print(remove_k_after_middle(list1, 0)) # 1 - 2 - 3 - 4 - 5 - 6
print(remove_k_after_middle(None, 2)) # None
