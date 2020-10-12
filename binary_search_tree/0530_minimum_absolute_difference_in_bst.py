"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        cur_min = int('inf')
        prev = -1

        def dfs(node):
            nonlocal prev, cur_min
            if not node:
                return

            dfs(node.left)
            if prev != -1:
                cur_min = min(node.val - prev, cur_min)
            prev = node.val
            dfs(node.right)

        dfs(root)

        return cur_min
