# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def traverse(root: TreeNode):
            nonlocal s, t, pred
            if not root:
                return

            traverse(root.left)
            if pred and root.val < pred.val:
                t = root
                if not s:
                    s = pred
                else:
                    return
            pred = root
            traverse(root.right)

        s = t = pred = None
        traverse(root)
        s.val, t.val = t.val, s.val
