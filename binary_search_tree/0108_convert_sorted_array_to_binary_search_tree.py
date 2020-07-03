"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def recurr(left, right):
            # recursion end point
            if left > right:
                return None
            # find mid point from left and right pointer
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = recurr(left, mid - 1)
            root.right = recurr(mid + 1, right)
            return root

        return recurr(0, len(nums) - 1)
