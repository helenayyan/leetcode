"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        if not rooms or not rooms[0]:
            return

        m = len(rooms)
        n = len(rooms[0])

        # classic graph dfs
        def fill_dist(i, j, dist):
            for x, y in DIRECTIONS:
                pos_x = x + i
                pos_y = y + j
                # movement decider: if shorter distance available for filling or not filled yet
                if 0 <= pos_x < m and 0 <= pos_y < n and rooms[pos_x][pos_y] > dist:
                    rooms[pos_x][pos_y] = dist
                    fill_dist(pos_x, pos_y, dist + 1)

        for p in range(m):
            for q in range(n):
                if rooms[p][q] == 0:
                    fill_dist(p, q, 1) # start from 0 with distance 1
