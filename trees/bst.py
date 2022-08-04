class BinarySearchTreeNode():
    def __init__(self, value=None):
        self.value = value
        self.left = None # All values on the left are smaller than self.value
        self.right = None # All values on the right are bigger than self.value

    def insert(self, value):
        """
        If the node doesn’t yet have a value, we can just set the given value and return.
        If we ever try to insert a value that also exists, we can also simply return as this can be considered a “no-op”.
        If the given value is less than our node’s value and we already have a left child then we recursively call insert on our left child.
        If we don’t have a left child yet then we just make the given value our new left child.
        Same but inverted for the right side.
        """
        if not self.value:
            self.value = value

        if self.value == value:

        if value < self.value:
            if self.left:
                self.left.insert(value)
            self.left = BinarySearchTreeNode(value)

        if self.right:
            self.right.insert(value)
        self.right = BinarySearchTreeNode(value)

    def size(self):
        """
        Get total number of nodes in tree.
        """
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size if self.right else 0
        return left_size + right_size + 1

    def max(self):
        """
        Recursively traverse the edges of the tree to find the largest values stored in the tree.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def min(self):
        """
        Recursively traverse the edges of the tree to find the smallest values stored in the tree.
        """
        current = self
        while current.right is not None:
            current = current.right
        return current

    def find(self, value):
        """
        Returns True or False, is the value in the BinarySearchTree
        """
        pass

    def height(self, value):
        pass

    # remove value

    def print_tree(self):
      print(self.data)

# recursion inside and outside of class


"""
PROS
- When balanced, a BST provides lightning-fast O(log(n)) insertions, deletions, and lookups
- BSTs are generally pretty simple, require little code to get running

CONS
- Slow for brute-force search. If we need to iterate over each node, an array may be faster
- When the tree becomes unbalanced, all fast O(log(n)) operations quickly degrade to O(n)
- Since pointers to whole objects are typically involved, a BST can require quite a bit more memory than an array, although this depends on the implementation.
"""
