'''
❓ PROMPT
Given a linked list, return the second to last element's value.

Example(s)
1 -> 2 => 1
1 -> 2 -> 3 -> 4 => 3


🔎 EXPLORE
State your assumptions & discoveries:
Q: If there is 1 or fewer node in the linked list, what should I return?
A: Return null.

Create examples & test cases:
# empty list
# 1-node list
# 2-node list
# odd-length list
# even-length list


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(N) to iterate through the length N list
Space: O(1) to store a constant number of variables


📆 PLAN
High-level outline of approach #:
Iterate through the linked list. Return the current's node's value if it's next.next is null.


🛠️ IMPLEMENT
function secondToLast(head) {
def secondToLast(head: Node) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def secondToLast(head: Node) -> int:

    if not head or not head.next:
        return None

    current = head

    while current.next.next:
        current = current.next

    return current.value

print(secondToLast(None) == None)

# 1
head = Node(1)
print(secondToLast(head) == None)

# 1 -> 2
head = Node(1, Node(2))
print(secondToLast(head) == 1)

# 1 -> 2 -> 3
head = Node(1, Node(2, Node(3)))
print(secondToLast(head) == 2)

# 1 -> 2 -> 3 -> 4
head = Node(1, Node(2, Node(3, Node (4))))
print(secondToLast(head) == 3)

# 1 -> 2 -> 3 -> 4 -> 5
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(secondToLast(head) == 4)
