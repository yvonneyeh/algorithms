'''
❓ PROMPT
Given a linked list and a target value, return the index of the first occurrence of that value in the linked list. The index should be zero-indexed.

Example(s)
list1 = 1 -> 2 -> 3 -> 4 -> 5

firstIndexInLL(list1, 9) == -1
firstIndexInLL(list1, 3) == 2


🔎 EXPLORE
State your assumptions & discoveries:

- Return -1 if it doesn't exist


Create examples & test cases:

# empty list
# 1 node list with target
# 1 node list without target
# list with all unique
# list with duplicates of target
# list without target


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(N) to iterate through the length N list
Space: O(1) to store a single variable


📆 PLAN
High-level outline of approach #:

Iterate through the linked list as normal, keeping a current index. When the value matches the target, return the current index.


🛠️ IMPLEMENT
function firstIndexInLL(node, target) {
def firstIndexInLL(node: Node, target: int) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def firstIndexInLL(node: Node, target: int) -> int:

    if not node:
        return -1

    index = 0
    current = node

    while current:
        if current.value == target:
            return index
        index += 1
        current = current.next
    return -1


list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
list2 = Node(2)
list3 = Node(-1, Node(-2, Node(-3, Node(-4, Node(-5)))))
list4 = Node(1, Node(2, Node(3, Node(2, Node(1)))))

print(firstIndexInLL(None, 12) == -1)
print(firstIndexInLL(list1, 9) == -1)
print(firstIndexInLL(list1, 3) == 2)
print(firstIndexInLL(list2, 2) == 0)
print(firstIndexInLL(list2, 1) == -1)
print(firstIndexInLL(list3, -2) == 1)
print(firstIndexInLL(list4, 2) == 1)
print(firstIndexInLL(list4, 1) == 0)
