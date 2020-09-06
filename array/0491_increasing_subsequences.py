"""

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.



Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
"""
from collections import defaultdict
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, tmp) -> None:
            if len(tmp) > 1:
                res.append(tmp)
            curPres = defaultdict(int)
            for inx, i in enumerate(nums):
                if curPres[i]:
                    continue
                if not tmp or i >= tmp[-1]:
                    curPres[i] = 1
                    dfs(nums[inx + 1:], tmp + [i])

        dfs(nums, [])
        return res
