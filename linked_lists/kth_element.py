'''
❓ PROMPT
Given a linked list and a target k, return a linked list containing every kth element.

Example(s)
head = 1 -> 3 -> 6 -> 2 -> 8 -> 9
everyKthNode(head, 3) == "6 -> 9"


🔎 EXPLORE
State your assumptions & discoveries:

Q: Should I modify the linked list in place or create a copy?
A: Create a copy.
Q: If the target is bigger than the length of the list, should I return null?
A: Yes.
Q: Can the target be less than 1?
A: No.


Create examples & test cases:

empty list
1 node list with target == 1
1 node list with target > 1
2 node list with target == 1
2 node list with target == 2
2 node list with target > 2
list with multiple nodes and is divisible by target
list with multiple nodes and is not divisible by target (there is remainder)


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(N) to iterate through the length N list
Space: O(k) to store k nodes in the new list


📆 PLAN
High-level outline of approach #:


🛠️ IMPLEMENT
function everyKthNode(node, target) {
def everyKthNode(node: Node, target: int) -> Node:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def everyKthNode(node: Node, target: int) -> Node:

    current = node
    result = Node(0)
    new = result

    while current:
        for i in range(1, target):
            current = current.next
            if current == None:
                return result.next

        new.next = Node(current.value)
        new = new.next
        current = current.next

    return result.next

    # current = node
    # result = Node(0)
    # result.next = None
    # count = 1

    # while current:
    #     if count % target == 0:
    #         result.next = Node(current.value)
    #         result.next.next = None
    #     current = current.next
    #     count += 1

    # return result.next

def toString(head: Node) -> None:
    if not head:
        return "<empty>"

    parts = []
    while head:
        parts.append(str(head.value))
        head = head.next

    result = " -> ".join(parts)
    print(result)
    return result

# 1 -> 3 -> 6 -> 2 -> 8 -> 9
head = Node(1, Node(3, Node(6, Node(2, Node(8, Node(9))))))
print(toString(everyKthNode(head, 3)) == "6 -> 9")
print(toString(everyKthNode(head, 1)) == "1 -> 3 -> 6 -> 2 -> 8 -> 9")
print(toString(everyKthNode(head, 5)) == "8")
print(toString(everyKthNode(head, 6)) == "9")
print(toString(everyKthNode(head, 7)) == "<empty>")

# 6
head = Node(6)
print(toString(everyKthNode(head, 1)) == "6")
print(toString(everyKthNode(head, 20)) == "<empty>")

# 6 -> 12
head = Node(6, Node(12))
print(toString(everyKthNode(head, 1)) == "6 -> 12")
print(toString(everyKthNode(head, 2)) == "12")

print(toString(everyKthNode(None, 5)) == "<empty>")
