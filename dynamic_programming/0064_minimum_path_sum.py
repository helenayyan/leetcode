"""

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n == 0 or m == 0:
            return 0
        dp = [[0 for _ in range(m)] for _ in range(n)]

        dp[0][0] = grid[0][0]

        # first row
        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        # first column
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, n):
            for j in range(1, m):
                # come from left block or upper block, choose the smaller one
                dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])

        return dp[-1][-1]
