'''
❓ PROMPT
Given integers *X* and *Y*, return the head of a linked list with *X* nodes with value *Y*.

Example(s)
createLL(5, 3)
"3 -> 3 -> 3 -> 3 -> 3"

createLL(6, 6)
"6 -> 6 -> 6 -> 6 -> 6 -> 6"

createLL(2, -10)
"-10 -> -10"


🔎 EXPLORE
State your assumptions & discoveries:

Q: Can X be negative?
A: No.
Q: If X is 0, should I return null?
A: Yes.

Create examples & test cases:

x = 0
x = 1
x = 2
x = 100
x == y
y = 0
y = -1


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(X) to generate a length X list
Space O(X) to store a length X list


📆 PLAN
High-level outline of approach #:
Start by returning null if X is null. Otherwise, create a head node with value Y. Then, create a curr pointer and iterate from 2 to X, adding a node to the end and moving curr forward.


- create Node class
-

🛠️ IMPLEMENT
function createLL(count, value) {
def createLL(count: int, val: int) -> Node:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def createLL(count: int, val: int) -> Node:

    if count == 0: return None

    dummy = Node(0)
    current = dummy

    while count > 0:
        current.next = Node(val)
        current = current.next
        count -= 1

    return dummy.next


def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.val))
    head = head.next

  return " -> ".join(parts)

print(toString(createLL(0, 1000)) == "<empty>")
print(toString(createLL(1, 999)) == "999")
print(toString(createLL(2, 88)) == "88 -> 88")
print(toString(createLL(3, 4)) == "4 -> 4 -> 4")
print(toString(createLL(5, 3)) == "3 -> 3 -> 3 -> 3 -> 3")
print(toString(createLL(6, 6)) == "6 -> 6 -> 6 -> 6 -> 6 -> 6")
print(toString(createLL(2, -10)) == "-10 -> -10")
print(toString(createLL(3, 0)) == "0 -> 0 -> 0")
