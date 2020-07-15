"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]

"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        def recur(left, right):
            result = []
            # recursion end point
            if left > right:
                return [None]

            # iterate through every number as node between the two pointer
            for i in range(left, right + 1):
                left_trees = recur(left, i - 1)
                right_trees = recur(i + 1, right)

                # append all the possibility to the result
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        node = TreeNode(i)
                        node.left = left_tree
                        node.right = right_tree
                        result.append(node)
            return result

        return recur(1, n)
