"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.

"""
from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        total = 0
        Direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n = len(grid)
        m = len(grid[0])
        shapes = []

        def findisland(i, j):
            grid[i][j] = 0
            for x, y in Direction:
                if 0 <= i + x < n and 0 <= j + y < m and grid[i + x][j + y] == 1:
                    curr_shape.append([x + i - curr_shape[0][0], y + j - curr_shape[0][1]])
                    findisland(i + x, j + y)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    curr_shape = [[i, j]]
                    findisland(i, j)
                    curr_shape[0] = [0, 0]
                    if curr_shape not in shapes:
                        shapes.append(curr_shape)
        print(shapes)

        return len(shapes)
