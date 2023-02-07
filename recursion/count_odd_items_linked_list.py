'''
Count The Odd Elements in a Linked List (recursive)

❓ PROMPT
Given a linked list of positive integers, count the elements with odd values from the list. Note that 0 is an even number.

Example(s)
head = 1 -> 1 -> 1 -> 1
countOdd(head) == 4

head = 1 -> 2 -> 3 -> 4
countOdd(head) == 2


🔎 EXPLORE
State your assumptions & discoveries:

- LL can be empty
- there may be no odd values


Create examples & test cases:

# empty list
# 1 node list with an odd value
# 1 node list without an odd value
# list with some odd values
# list with no odd values


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(N) to iterate through the length N list
Space: O(N) to store N call frames on the stack


📆 PLAN
High-level outline of approach #:

At each node, if the current value is odd, return 1 plus the value returned from calling the function on the next node. Return 0 as a base case if the current node is null.


🛠️ IMPLEMENT
function countOdd(head) {
def countOdd(head: Node) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def countOdd(head: Node) -> int:

    current = head
    count = 0

    if not current:
        print("not current")
        return 0
    else:
        count = countOdd(current.next)
        print(count)

    return count + 1 if current.value % 2 == 1 else count


print(countOdd(None) == 0)

# 0
head = Node(0)
print(countOdd(head) == 0)

# 5
head = Node(5)
print(countOdd(head) == 1)

# 6
head = Node(6)
print(countOdd(head) == 0)

# 1 -> 1 -> 1 -> 1
head = Node(1, Node(1, Node(1, Node(1))))
print(countOdd(head) == 4)

# 1 -> 2 -> 3 -> 4
head = Node(1, Node(2, Node(3, Node(4))))
print(countOdd(head) == 2)

# 2 -> 2 -> 2 -> 2
head = Node(2, Node(2, Node(2, Node(2))))
print(countOdd(head) == 0)

# 1 -> 2 -> 3 -> 4 -> 5
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(countOdd(head) == 3)

# 6 -> 2 -> 100 -> 4 -> 8
head = Node(6, Node(2, Node(100, Node(4, Node(8)))))
print(countOdd(head) == 0)
