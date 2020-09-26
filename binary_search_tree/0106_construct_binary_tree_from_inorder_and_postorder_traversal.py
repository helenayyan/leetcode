"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def dfs(i, j):
            # i, j are both closed end boundary
            if i > j:
                return None

            # the last value in postorder is the current root value
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # divide the inorder traversal list into left and right tree
            root_index = inorder.index(root_val)

            # construct right subtree first
            root.right = dfs(root_index + 1, j)
            # then construct left subtree
            root.left = dfs(i, root_index - 1)

            return root

        n = len(inorder)

        return dfs(0, n - 1)
