"""
Q. Given a linked list, sum all elements in the list.

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 // returns 10
• Given a linked list: 1 // returns 1
"""

class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value} -> {self.next.value}"

    def __repr__(self):
        head = self
        l = []
        while head:
            l.append(head.value)
            head = head.next
        return f'<Node: {l}>'

def sum(node: ListNode) -> int:
    curr = node
    if curr == None:
        return 0

    result = curr.value + sum(curr.next)
    # print("curr", curr.value)
    # print("result", result)
    print(curr)

    return result

# 1 + sum(4->5)
# 4 + sum(5)
# 5 + sum(None)
# 0

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
# print(sum(None)) # 0
print(sum(LL1)) # 10
# print(sum(ListNode(1))) # 1
