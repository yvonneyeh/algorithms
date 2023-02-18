'''
❓ PROMPT
Given a linked list, return the number of values that occur exactly twice.

Example(s)
head = 1 -> 2 -> 2 -> 3 -> 3 -> 3
numPairs(head) == 1


🔎 EXPLORE
State your assumptions & discoveries:


Create examples & test cases:


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O()
Space: O()


📆 PLAN
High-level outline of approach #:


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
