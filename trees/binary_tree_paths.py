# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Input: root = [1]
# Output: ["1"]


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []

        result = []
        self.dfs(root, "", result)
        return result

    def dfs(self, root, path, result):
        # recursive depth first search
        if not root.left and not root.right:
            result.append(path + str(root.val))

        if root.left:
            self.dfs(root.left, path + str(root.val) + "->" , result)
        if root.right:
            self.dfs(root.right, path + str(root.val) + "->", result)
