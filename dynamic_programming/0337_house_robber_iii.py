"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root):
            if not root:
                return [0, 0]
            left_node = root.left
            right_node = root.right
            [left_rob, left_not_rob] = dfs(left_node)
            [right_rob, right_not_rob] = dfs(right_node)
            return [root.val + left_not_rob + right_not_rob,
                    max(left_rob, left_not_rob) + max(right_rob, right_not_rob)]

        return max(dfs(root))
