# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        level = deque()
        level.append(root)

        while level:
            curr_level = []
            # store the length of current level (unnecessary for python but needed for other language
            a = len(level)
            for _ in range(a):  # traversal the current level
                node = level.popleft()
                curr_level.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            result.append(list(curr_level))
        result = result[::-1]
        return result
