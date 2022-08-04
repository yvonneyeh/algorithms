# Runtime = O(n)

class BinaryTreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None # (almost) ALWAYS be nodes
        self.right = None # (almost) ALWAYS be nodes

    def longest_string(self):
        longest_left = self.left.longest_string() if self.left else ""
        longest_right = self.right.longest_string() if self.right else ""

        return max(
                (len(self.value), self.value),
                (len(longest_left), longest_left),
                (len(longest_right), longest_right)
        )[1]

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return max(left_height, right_height) + 1

    def size(self):
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return left_size + right_size + 1

def size_of_binary_tree(node):
    if not node:
        return 0
    else:
        return size_of_binary_tree(node.left) + size_of_binary_tree(node.right) + 1


def minimum_of_binary_tree(node):
    if not node:
        return ""
    else:
        return min(node.value, minimum_of_binary_tree(node.left), minimum_of_binary_tree(node.right))

r = BinaryTreeNode("root")
r.left = BinaryTreeNode("root.left")
r.left.right = BinaryTreeNode("root.left.right")
r.left.right.left = BinaryTreeNode("yaniv")
r.right = BinaryTreeNode("root.right")
r.right = BinaryTreeNode("root.right")
r.right.right = BinaryTreeNode("root.right.right")
r.right.right.left = BinaryTreeNode("yvonne")

print(size_of_binary_tree(r))
print(size_of_binary_tree(r.left))
