'''
❓ PROMPT
Given a linked list, return an array with all the elements in reverse.

Example(s)
head = 1 -> 3 -> 5 -> 2
createArrayInReverse(head) == [2,5,3,1]


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
function createArrayInReverse(node) {
def createArrayInReverse(node: Node) -> list[int]:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def createArrayInReverse(node: Node) -> list[int]:

    if not node:
        return []

    result = []

    while node:
        result.append(node.value)
        node = node.next

    l = 0
    r = len(result)-1

    while l < r:
        result[l], result[r] = result[r], result[l]
        l += 1
        r -= 1

    return result



    # if not node:
    #     return []

    # prev = None
    # head = node
    # current = node
    # result = []

    # while current:
    #     original_next = current.next
    #     current.next = prev
    #     prev = current
    #     current = original_next

    # while head:
    #     result.append(head.value)
    #     head = head.next

    # print(result)
    # return result

# 1 -> 3 -> 5 -> 2
head = Node(1, Node(3, Node(5, Node(2))))
print(createArrayInReverse(head) == [2, 5, 3, 1])

# 4 -> 9 -> 14
head = Node(4, Node(9, Node(14)))
print(createArrayInReverse(head) == [14, 9, 4])

# 5 -> 10 -> 15 -> 20
head = Node(5, Node(10, Node(15, Node(20))))
print(createArrayInReverse(head) == [20, 15, 10, 5])

# 5
head = Node(5)
print(createArrayInReverse(head) == [5])

# 5 -> 10
head = Node(5, Node(10))
print(createArrayInReverse(head) == [10, 5])

# 5 -> 5 -> 10 -> 10
head = Node(5, Node(5, Node(10, Node(10))))
print(createArrayInReverse(head) == [10, 10, 5, 5])

# 5 -> 5 -> 5
head = Node(5, Node(5, Node(5)))
print(createArrayInReverse(head) == [5, 5, 5])

# 0
head = Node(0)
print(createArrayInReverse(head) == [0])

# None
head = None
print(createArrayInReverse(head) == [])
