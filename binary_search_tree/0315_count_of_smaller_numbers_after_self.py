"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 1  # number of elements obtain same value at this node
        self.pos = 0  # number of nodes in its left branch


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        root = None
        if len(nums) == 0:
            return []

        # create binary search tree and check the position of each element
        def checkPos(node, num):
            # if num is larger, put into right branch, vice versa
            if node.val < num:
                if not node.right:
                    # create right node
                    right_node = TreeNode(num)
                    node.right = right_node
                    # return number of all elements of left branch and root
                    return node.count + node.pos
                else:
                    return node.count + node.pos + checkPos(node.right, num)
            elif node.val > num:
                node.pos += 1  # add one to left branch
                if not node.left:
                    # so far the smallest, create left node
                    left_node = TreeNode(num)
                    node.left = left_node
                    return 0
                else:
                    return checkPos(node.left, num)
            else:
                # if node value == num, no need to create a new node but add one to the node.count
                node.count += 1
                return node.pos

        for num in reversed(nums):
            # start point: last element must have result 0
            if not root:
                root = TreeNode(num)
                result.append(0)
            else:
                result.append(checkPos(root, num))

        return result[::-1]
