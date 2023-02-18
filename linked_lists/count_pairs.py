'''
❓ PROMPT
Given a linked list, return the number of values that occur exactly twice.

Example(s)
head = 1 -> 2 -> 2 -> 3 -> 3 -> 3
numPairs(head) == 1


🔎 EXPLORE
State your assumptions & discoveries:

Q: Can the list be empty?
A: Yes.
Q: What should I do when a number appears an even number of times?
A: Don't count it as a pair. There have to be exactly 2.


Create examples & test cases:

empty list
1 node list
2 node list with unique values
2 node list with the same value
list with a pair
list with multiple pairs
list with multiple duplicates
list with pairs and multiple duplicates
list with a number that appears 3 times
list with a number that appears more than twice and the frequency is divisible by two


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(N) to iterate through the length N list
Space O(N) to count N nodes and their frequencies


📆 PLAN
High-level outline of approach #:

Create a dictionary of counts and a count variable. Iterate through the linked list, incrementing the count of each value as you see it.
Option 1: Whenever the count becomes 2, increment the count variable. Whenever the count becomes 3, decrement the count variable (because it was overcounted earlier). Note that once the count becomes 3, it doesn't matter to increment the count beyond that.
Option 2: Create a follow-up loop going through all of the values and count the number of 2's.


🛠️ IMPLEMENT
function numPairs(head) {
def numPairs(head: Node) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def numPairs(head: Node) -> int:

    if not head:
        return 0

    current = head
    counts = {}

    while current:
        counts[current.value] = counts.get(current.value, 0) + 1
        current = current.next

    pairs = [i for i in counts if counts[i] == 2]

    return len(pairs)

head1 = Node(1, Node(2, Node(2, Node(3, Node(3, Node(3))))))
head2 = Node(5, Node(5, Node(10, Node(20))))
head3 = Node(5, Node(5, Node(10, Node(10))))
head4 = Node(5, Node(5, Node(5, Node(10))))
head5 = Node(5, Node(10, Node(10, Node(10))))
head6 = Node(4)
head7 = Node(5, Node(5))
head8 = Node(5, Node(5, Node(5, Node(5))))
head9 = Node(6, Node(9))
head10 = Node(5, Node(5, Node(5, Node(10, Node(10)))))
head11 = Node(6, Node(5, Node(5, Node(5, Node(5, Node(6))))))

print(numPairs(None) == 0)
print(numPairs(head1) == 1)
print(numPairs(head2) == 1)
print(numPairs(head3) == 2)
print(numPairs(head4) == 0)
print(numPairs(head5) == 0)
print(numPairs(head6) == 0)
print(numPairs(head7) == 1)
print(numPairs(head8) == 0)
print(numPairs(head9) == 0)
print(numPairs(head10) == 1)
print(numPairs(head11) == 1)
