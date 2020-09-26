# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(node, target):
            if not node:
                return
            path.append(node.val)

            if not node.left and not node.right and node.val == target:
                res.append(path[:])
            else:
                target -= node.val
                dfs(node.left, target)
                dfs(node.right, target)
            path.pop()
            return

        dfs(root, sum)
        return res
