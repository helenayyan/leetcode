# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        result = []
        level = deque()
        level.append(root)

        while level:
            curr_level = []
            a = len(level)

            for _ in range(a):
                node = level.popleft()
                curr_level.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            result.append(sum(curr_level) / a)

        return result
