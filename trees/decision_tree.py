"""
A decision tree is a data structure that can be evaluated on a set of signals and return a decision (e.g. Yes or No ("Y" or "N")). Each interior node of the tree is associated with a particular signal and a constant value against which to compare that signal, and each leaf node has a value which will be returned by the tree. To evaluate the tree on a set of signals we traverse the tree, starting at the root and comparing the appropriate signal value to the constant associated with each interior node. If the signal value is less than the constant we proceed down the left subtree and if it is greater than or equal to the constant we proceed down the right subtree. We continue until we reach a leaf at which point we return the value associated with the leaf.

For example, suppose that we have a set of integer-valued signals {X1, X2, X3}. Consider the following decision tree:

           X1 < 3
        ------------
       |            |
    X2 < 1       X1 < 6
 -----------    ---------
|           |  |         |
N           Y  N      X3 < 2
                    ----------
                   |          |
                   Y          N

If we evaluate this tree on signals {X1: 2, X2: 1, X3: 11} the result will be Y. Evaluating on signals {X1: 8, X2: 4, X3: 12} we get N. We can use these to implement decisions that need to be made repeatedly on different input values. For instance, a given decision tree might represent a rule to decide whether or not a given transaction looks fraudulent, and the signals could represent different quantities like X1) the age of the account in days, X2) the dollar value of the transaction, and X3) the time in hours since the last transaction attempt.

In real life, we would probably grow a decision tree via some machine learning algorithm. In this exercise, however, we will manually create the tree that we want. We can grow a decision tree by starting with a single-leaf tree and recursively splitting the leaves of the tree. We do this by associating a split condition to a node, creating two new leaves below it, and associating a return value to each of those leaves.

So to grow the tree above we start with a single-leaf tree:

Y

Then add the split condition X1 < 3 and (optionally) assign return values to the new leaves:

     X1 < 3
  ------------
 |            |
 Y            N

Then add a split condition to the left leaf:

           X1 < 3
        ------------
       |            |
    X2 < 1          N
 -----------
|           |
X           X

Assign return values to the new leaves:

           X1 < 3
        ------------
       |            |
    X2 < 1         N
 -----------
|           |
N           Y

And so on until we are done.

The goal of this question is to implement a decision tree that can be grown incrementally in this fashion and evaluated on a particular set of signals. Concretely you should implement the following pseudocode API in the language of your choice:

class DecisionTree:

  method add_split(leaf, signal_name, constant):
    Add a split condition to the given leaf node.
    Return the newly created leaves for future calls.
    Feel free to pass a sentinel value (like null) as the leaf for the first call to this method.
    Subsequent calls should pass leaves returned by previous calls.

  method set_leaf_value(leaf, value):
    Set the return value for a leaf node.

  method evaluate(signals):
    Evaluate the tree on a mapping of signal_name -> signal_value.
    Return the value of the leaf node reached by traversing the tree.

Afterwards, use your solution to grow the example tree above and write some test cases.

dt = DecisionTree()

root_pass, root_fail = dt.add_split(None, "X1", 3)

dt.set_leaf_value(root_pass, "Y")
dt.set_leaf_value(root_fail, "N")

left_pass, left_fail = dt.add_split(root_pass, "X2", 1)

dt.set_leaf_value(left_pass, "N")
dt.set_leaf_value(left_fail, "Y")


"""




"""
1. How are we making the problem smaller (most abstract sense)?
    We look at smaller parts of the tree
2. If we keep making the problem smaller, at what point do we just know the answer?
    - There is no tree
    - There are no children (it is a leaf)
3. Write out the base case
4. Write out the recursive call (and only the recursion) (Assume we have a magic function that will work for our childern. Call it)
    - self.left.maximum()
    - self.right.maximum()
5. Finish the function
"""

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


class DecisionTreeNode():
    def __init__(self):
        self.leaf_value = "X" # If it is an empty string, then the node is not a leaf
        self.signal_name = ""
        self.constant = 0

        self.left = None
        self.right = None

    def split(self, signal_name, constant):
        self.leaf_value = ""
        self.signal_name = signal_name
        self.constant = constant
        self.left = DecisionTreeNode()
        self.right = DecisionTreeNode()
        return self.left, self.right


    def evaluate(self, signals):
        if self.leaf_value:
            return self.leaf_value
        else:
            if signals[self.signal_name] < self.constant:
                return self.left.evaluate(signals)
            else:
                return self.right.evaluate(signals)

    def __repr__(self) -> str:
        if self.leaf_value:
            return self.leaf_value
        else:
            return f"({self.signal_name} < {self.constant} ({self.left}, {self.right}))"


class DecisionTree:
    def __init__(self):
        self.root = DecisionTreeNode()

    def add_split(self, leaf, signal_name, constant):
        """
        Add a split condition to the given leaf node.
        Return the newly created leaves for future calls.
        Feel free to pass a sentinel value (like null) as the leaf for the first call to this method.
        Subsequent calls should pass leaves returned by previous calls.
        """
        if not leaf:
            leaf = self.root

        return leaf.split(signal_name, constant)

    def set_leaf_value(self, leaf, value):
        """
        Set the return value for a leaf node.
        """
        leaf.leaf_value = value

    def evaluate(self, signals):
        """
        Evaluate the tree on a mapping of signal_name -> signal_value.
        Return the value of the leaf node reached by traversing the tree.
        """
        return self.root.evaluate(signals)

    def __repr__(self) -> str:
        return str(self.root)



dt = DecisionTree()
root_pass, root_fail = dt.add_split(None, "X1", 3)
dt.set_leaf_value(root_pass, "Y")
dt.set_leaf_value(root_fail, "N")
left_pass, left_fail = dt.add_split(root_pass, "X2", 1)
dt.set_leaf_value(left_pass, "N")
dt.set_leaf_value(left_fail, "Y")

print(dt)

print(dt.evaluate({"X1": 0, "X2": 0}))      # N
print(dt.evaluate({"X1": 10, "X2": 0}))     # N
print(dt.evaluate({"X1": 0, "X2": 10}))     # Y
print(dt.evaluate({"X1": 10, "X2": 10}))    # N































class DecisionTree2:
    def __init__(self):
        self.root = DecisionTreeNode()

    def add_split(self, leaf, signal_name, constant):
        if not leaf:
            leaf = self.root

        leaf.leaf_value = ""
        leaf.signal_name = signal_name
        leaf.constant = constant
        leaf.left = DecisionTreeNode()
        leaf.right = DecisionTreeNode()
        return leaf.left, leaf.right

    def set_leaf_value(self, leaf, value):
        leaf.leaf_value = value

    def _evaluate_helper(self, node, signals):
        if node.leaf_value:
            return node.leaf_value
        else:
            if signals[node.signal_name] < node.constant:
                return self._evaluate_helper(node.left, signals)
            else:
                return self._evaluate_helper(node.right, signals)

    def evaluate(self, signals):
        return self._evaluate_helper(self.root, signals)

    def __repr__(self) -> str:
        return str(self.root)



    # def maximum(self):
    #     if not self.left and not self.right:
    #         return self.value
    #     else:
    #         left = self.left.maximum() if self.left else self.value
    #         right = self.right.maximum() if self.right else self.value
    #         return max(self.value, left, right)


# def maximum_of_binary_tree(node) -> str:
#     if not node:
#         return ""

#     return max(node.value, maximum_of_binary_tree(node.left), maximum_of_binary_tree(node.right))
