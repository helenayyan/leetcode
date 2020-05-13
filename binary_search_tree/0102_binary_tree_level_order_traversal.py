"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode) -> [[int]]:
    # if the tree is empty
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
        result.append(curr_level)
    return result
