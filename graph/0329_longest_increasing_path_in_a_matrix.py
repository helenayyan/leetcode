"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # exception
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)  # row
        m = len(matrix[0])  # column

        # create memo to store results
        memo = [[0 for _ in range(m)] for _ in range(n)]

        def dfs(i, j):
            # if node already visited
            if memo[i][j]:
                return memo[i][j]

            res = 1
            # direction vectors
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for direction in directions:
                x = i + direction[0]
                y = j + direction[1]

                # follow increasing path
                if 0 <= x < n and 0 <= y < m and matrix[x][y] > matrix[i][j]:
                    res = max(res, 1 + dfs(x, y))

                # store the longest increasing path from this node
                memo[i][j] = max(memo[i][j], res)
            return memo[i][j]

        result = 0
        for i in range(n):
            for j in range(m):
                # iterate through all nodes
                result = max(result, dfs(i, j))

        return result

    # method 2 with decorator
    def longestIncreasingPathWithDecorator(self, matrix: List[List[int]]) -> int:
        # exception
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)  # row
        m = len(matrix[0])  # column

        # create memo to store results
        @lru_cache(None)
        def dfs(i, j):

            res = 1
            # direction vectors
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for direction in directions:
                x = i + direction[0]
                y = j + direction[1]

                # follow increasing path
                if 0 <= x < n and 0 <= y < m and matrix[x][y] > matrix[i][j]:
                    res = max(res, 1 + dfs(x, y))
            return res

        result = 0
        for i in range(n):
            for j in range(m):
                # iterate through all nodes
                result = max(result, dfs(i, j))

        return result
