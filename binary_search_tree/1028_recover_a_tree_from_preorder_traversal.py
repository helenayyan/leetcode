"""
input："1-2--3--4-5--6--7"
output：[1,2,5,3,4,6,7]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack = []
        pos = 0
        while pos < len(S):
            level = 0
            # read the level of the value
            while S[pos] == "-":
                level += 1
                pos += 1

            value = 0
            # read the value from the string
            while pos < len(S) and S[pos].isdigit():
                value = value * 10 + (ord(S[pos]) - ord('0'))
                pos += 1

            node = TreeNode(value)
            if len(stack) == 0:
                stack.append(node)
                continue

            # find father node using level stored
            while len(stack) > level:
                stack.pop()

            # decide whether left son or right son
            if stack[-1].left:
                stack[-1].right = node
            else:
                stack[-1].left = node
            stack.append(node)

        return stack[0]
