"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        res = []
        last = TreeNode(None)
        most = 0
        count = 0

        def inorder_dfs(root):
            nonlocal res, last, most, count
            if not root:
                return
            inorder_dfs(root.left)
            if root.val == last.val:
                count += 1
            else:
                count = 1
            if count > most:
                most = count
                res = [root.val]
            elif count == most:
                res.append(root.val)
            last = root
            inorder_dfs(root.right)

        inorder_dfs(root)
        return res
