"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/burst-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0

        # add front end balloons num = 1
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        nums = [1] + nums + [1]

        # reversed dp
        for left in range(n, -1, -1):
            for right in range(left + 1, n + 2):
                for i in range(left + 1, right):
                    # find the maximum value for this interval
                    dp[left][right] = max(dp[left][right],
                                          nums[i] * nums[left] * nums[right] + dp[left][i] + dp[i][right])

        return dp[0][-1]
