# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        def dfs(node):
            if not node:
                return

            left_node = node.left
            right_node = node.right
            node.right = left_node
            node.left = right_node
            dfs(node.right)
            dfs(node.left)

        dfs(root)
        return root
