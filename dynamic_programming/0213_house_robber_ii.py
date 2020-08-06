"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        # only two more cases when looped
        case1 = self.rob_range(nums[1:])
        case2 = self.rob_range(nums[:-1])
        return max(case1, case2)

    # as from 0198 house robber
    def rob_range(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        prev_rob = nums[0]
        prev_not_rob = 0

        for i in range(1, n):
            curr_rob = prev_not_rob + nums[i]
            prev_not_rob = max(prev_not_rob, prev_rob)
            prev_rob = curr_rob
        return max(prev_rob, prev_not_rob)