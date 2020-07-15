"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        # from bottom to top, O(N^2)
        level = triangle[-1]
        for item in reversed(triangle[:-1]):
            store = []
            for i, num in enumerate(item):
                store.append(min(num + level[i], num + level[i + 1]))
            level = store

        return level[0]

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        # from bottom to top, O(1)
        dp = triangle[-1]
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1]);

        return dp[0]

    """
            From：LeetCode - Solution
            Link: https://leetcode-cn.com/problems/triangle/solution/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/

    """

    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        # from top to bottom, O(N^2)
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        return min(dp[n - 1])

    def minimumTotal4(self, triangle: List[List[int]]) -> int:
        # from top to bottom, O(N)
        n = len(triangle)
        f = [[0] * n for _ in range(2)]
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            curr, prev = i % 2, 1 - i % 2
            f[curr][0] = f[prev][0] + triangle[i][0]
            for j in range(1, i):
                f[curr][j] = min(f[prev][j - 1], f[prev][j]) + triangle[i][j]
            f[curr][i] = f[prev][i - 1] + triangle[i][i]

        return min(f[(n - 1) % 2])
