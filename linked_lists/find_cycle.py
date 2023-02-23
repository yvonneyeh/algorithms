# Linked lists

# (Node A) -> (Node B -> None)

from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: 'Node' = None

    @property
    def as_list(self):
        if not self:
            return []

        converted_list = []
        cur = self
        while cur:
            converted_list.append(cur.value)
            cur = cur.next

        return converted_list

    @classmethod
    def from_list(cls, l):
        sentinel = cls(0)
        curr = sentinel
        for element in l:
            curr.next = cls(element)
            curr = curr.next
        return sentinel.next


# 1. list to linked list
def createLL(arr: list[int]) -> Node:
    sentinel = Node(0)
    curr = sentinel
    for element in arr:
        curr.next = Node(element)
        curr = curr.next
    return sentinel.next

def createLL2(arr: list[int]) -> Node:
    if not arr:
        return None
    head = curr = Node(arr[0])
    for element in arr[1:]:
        curr.next = Node(element)
        curr = curr.next
    return head

# print(createLL([1, 2, 3, 4, 5, 6, 7, 8]))
# print(createLL([])) # => None

# print(createLL2([1, 2, 3, 4, 5, 6, 7, 8]))
# print(createLL2([])) # => None

# 2. linked list to list

def ll_to_list(ll: Node) -> list[int]:
    if not ll:
        return []

    converted_list = []
    cur = ll
    while cur:
        converted_list.append(cur.value)
        cur = cur.next

    return converted_list

print(ll_to_list(createLL([1, 2, 3, 4, 5, 6, 7, 8])))
print(ll_to_list(createLL([])))


# [ ] Deleting or disconnecting a node from a linked list
# [Y, D, J] Detecting if there's a cycle in a linked list
# [Y, A, D, J] Simulating stacks & queues



# cycle
list_with_cycle = Node(1, Node(2))
# print(id(list_with_cycle))
list_with_cycle.next.next = list_with_cycle
# print(id(list_with_cycle))

# print(list_with_cycle)

# if values are unique, track values using a set -- make sure there's no repeats
# ++++ if values are not unique, track ids -- make sure there's no repeats

# has_
# is_
def ll_has_cycle(ll):
    s = set()
    cur = ll
    while cur:
        if id(cur) in s:
            return True
        s.add(id(cur))
        print(cur.value)
        cur = cur.next # moving to the next node
    return False

print('---------------------')
print(ll_has_cycle(list_with_cycle))

list_with_no_cycle = Node(3, Node(4, Node(5)))

print(ll_has_cycle(list_with_no_cycle))

# function cycle(head) {
#     let slow = head;
#     let fast = head.next;

#     while (fast && fast.next) {
#         if (slow == fast) {
#             return true;
#         }
#         slow = slow.next;
#         fast = fast.next.next;
#     }
#     return false;
# }
