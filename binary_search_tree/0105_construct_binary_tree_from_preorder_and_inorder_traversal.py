"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(i, j):
            if i > j:
                return None

            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            root_index = inorder.index(root_val)
            root.left = dfs(i, root_index - 1)
            root.right = dfs(root_index + 1, j)

            return root

        return dfs(0, len(inorder) - 1)
