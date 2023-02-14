'''
❓ PROMPT
Given a linked list of sequential, ascending numbers, return the first missing value or the next value that should be in the list. For any node, the next value could be 1 or 2 greater than the current node's value.

Furthermore, the list doesn't necessarily begin at 1.

Example(s)
head1 = 1 -> 3
findMissing(head1) == 2

head2 = -3 -> -1
findMissing(head2) == -2

head3 = 5 -> 6 -> 7 -> 8 -> 9
findMissing(head3) == 10

head4 = 5 -> 6 -> 7 -> 8 -> 10
findMissing(head4) == 9


🔎 EXPLORE
State your assumptions & discoveries:

Q: What if the list is empty?
A: Return 1

Q: What if the list has all consecutive numbers?
A: Return the number that should come after the tail

Q: Will the list contain only integers?
A: Yes.

Q: Can the numbers be negative?
A: Yes.

Create examples & test cases:

empty list
1-node list
list with all consecutive numbers
list skipping a number
list skipping a number on the second-to-last node
list skipping a number on the second node

🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(N) to iterate through the length N list
Space: O(1) to store a constant number of variables


📆 PLAN
High-level outline of approach #:

If the list is empty, return 1.
Otherwise initialize a variable to the first value.
Starting at the second node, check to see if that node's value is one greater and update the variable.
If it is not (or if there is no second node) return the value in the variable plus 1.


🛠️ IMPLEMENT
class Node {
  constructor(val, next=null) {
    this.val = val
    this.next = next
  }
}

function findMissing(head) {

class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

def findMissing(head: Node) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

def findMissing(head: Node) -> int:

    if not head:
        return 1

    current = head

    while current.next:
        if current.value + 1 != current.next.value:
            return current.value + 1

        current = current.next

    # only 1 node exists OR all nodes are sequential
    return current.value + 1

head1 = Node(1, Node(3))
head2 = Node(-3, Node(-1))
head3 = Node(5, Node(6, Node(7, Node(8, Node(9)))))
head4 = Node(5, Node(6, Node(7, Node(8, Node(10)))))
head5 = Node(1)
head6 = Node(10)
head7 = Node(1, Node(2))
head8 = Node(5, Node(6, Node(8, Node(9, Node(10)))))
head9 = Node(5, Node(7, Node(8, Node(9, Node(10)))))
head10 = Node(-1)

print(findMissing(head1) == 2)
print(findMissing(head2) == -2)
print(findMissing(head3) == 10)
print(findMissing(head4) == 9)
print(findMissing(head5) == 2)
print(findMissing(head6) == 11)
print(findMissing(head7) == 3)
print(findMissing(head8) == 7)
print(findMissing(head9) == 6)
print(findMissing(head10) == 0)
print(findMissing(None) == 1)
