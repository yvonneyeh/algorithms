'''
❓ PROMPT
Given an array containing numbers, convert this to a singly linked list and return the head of the list.

Example(s)
arrayToLL([1,2]) == "1 -> 2"
arrayToLL([1,2,3]) == "1 -> 2 -> 3"


🔎 EXPLORE
State your assumptions & discoveries:


Create examples & test cases:

# empty array
# array with 1 element
# odd length array
# even length array
# array with duplicate values


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.

Approach 1:
Time: O(n) to iterate through the n length array
Space O(n) to store n elements into nodes


📆 PLAN
High-level outline of approach #:

Create a dummy/sentinel node in a variable, and also a curr variable set to the same place. Iterate through the array creating new nodes and updating curr to always point to the most recently created node. At the end, return dummy.next to be the head.


🛠️ IMPLEMENT
function arrayToLL(array) {
def arrayToLL(array: list[int]) -> Node:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        print(f"{self.data} -> {self.next}")

def arrayToLL(array: list[int]) -> Node:
    dummy = Node(0)
    current = dummy

    for i, value in enumerate(array):
        current.next = Node(value)
        current = current.next

    return dummy.next


def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.data))
    head = head.next

  return " -> ".join(parts)

print(toString(arrayToLL([])) == "<empty>")
print(toString(arrayToLL([1])) == "1")
print(toString(arrayToLL([1,2])) == "1 -> 2")
print(toString(arrayToLL([1,2,3])) == "1 -> 2 -> 3")
print(toString(arrayToLL([5,0,3])) == "5 -> 0 -> 3")
print(toString(arrayToLL([8,7,8,8])) == "8 -> 7 -> 8 -> 8")
print(toString(arrayToLL([8,7,8,8,7])) == "8 -> 7 -> 8 -> 8 -> 7")
