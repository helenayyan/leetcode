# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(root1, root2):
            if not root1 or not root2:
                return not root2 and not root1
            if root1.val != root2.val:
                return False
            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)

        return dfs(p, q)
