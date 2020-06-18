"""
input: [1,null,2,3]
   1
    \
     2
    /
   3

output: [1,2,3]
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        level = []
        if not root:
            return res
        level.append(root)
        while level:
            curr_level = []
            node = level.pop()
            if node:
                res.append(node.val)
                level.append(node.right)
                level.append(node.left)
        return res
