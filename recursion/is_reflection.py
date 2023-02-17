from typing import Any


class Node:
    def __init__(self, value: Any, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    # def __repr__(self):
    #     print(f"{self.value} -> {self.left}, {self.right}")

def is_reflection(tree) -> bool:
    if not tree:
        print("hola")
        return True

    def is_match(n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        else: # both n1 and n2 exist
            if n1.value != n2.value:
                return False
            return is_match(n1.left, n2.right) and is_match(n1.right, n2.left)

    return is_match(tree, tree)




t1 = Node(0, Node(1), Node(1))
t2 = Node(0, Node(2), Node(1))
t3 = Node(0, Node(1, Node(1), Node(1)), Node(1, Node(1), Node(1)))
t4 = Node(0, Node(1, Node(1), Node(2)), Node(1, Node(2), Node(1)))
t5 = Node(0, Node(1, Node(1), Node(2)), Node(1, Node(1), Node(2)))
t6 = Node(0, Node(1, Node(1), Node(None)), Node(1, Node(None), Node(1)))


print(is_reflection(t1)) # T
print(is_reflection(t2)) # F
print(is_reflection(t3)) # T
print(is_reflection(t4)) # T
print(is_reflection(t5)) # F
print(is_reflection(t6)) # T
print(is_reflection(None))
