"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        if not pre:
            return None

        root = TreeNode(pre[0])

        # bottom node
        if len(pre) == 1:
            return root

        # length of left subtree
        num_nodes = post.index(pre[1]) + 1

        root.left = self.constructFromPrePost(pre[1:num_nodes + 1], post[:num_nodes])
        root.right = self.constructFromPrePost(pre[num_nodes + 1:], post[num_nodes:-1])
        return root
