"""
input: [1,null,2,3]
   1
    \
     2
    /
   3

output: [3, 2, 1]
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        level = []
        if not root:
            return res
        level.append(root)
        while level:
            node = level.pop()
            if node:
                res.append(node.val)
                level.append(node.left)
                level.append(node.right)
        return res[::-1]
