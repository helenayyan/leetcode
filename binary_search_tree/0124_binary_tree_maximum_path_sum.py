"""
input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

output: 42
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # outer scope variable needed
        self.sum_max = root.val

        def dfs(root):
            if not root:
                return 0

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            self.sum_max = max(self.sum_max, left + right + root.val)
            return root.val + max(left, right)

        dfs(root)
        return self.sum_max
