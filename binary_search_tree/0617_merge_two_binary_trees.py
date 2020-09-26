"""
Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(t1_node, t2_node):
            if not t1_node and not t2_node:
                return None
            elif not t1_node:
                return t2_node
            elif not t2_node:
                return t1_node
            else:
                merge_node = TreeNode(t1_node.val + t2_node.val)
                merge_node.left = dfs(t1_node.left, t2_node.left)
                merge_node.right = dfs(t1_node.right, t2_node.right)
                return merge_node

        return dfs(t1, t2)
