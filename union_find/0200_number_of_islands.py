"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])

        count = 0  # number of islands 

        def dfs(i, j):
            direction = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
            for x, y in direction:
                if 0 <= x < n and 0 <= y < m and grid[x][y] == '1':
                    grid[x][y] = '2'
                    dfs(x, y)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
