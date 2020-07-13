"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

"""
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[1 for _ in range(m)] for _ in range(n)]

        dp[n - 1][m - 1] = -dungeon[n - 1][m - 1] + 1  # max life needed to survive in the last block
        if dungeon[n - 1][m - 1] > 0:
            dp[n - 1][m - 1] = 1
        # last row
        for i in range(m - 2, -1, -1):
            dp[n - 1][i] = max(dp[n - 1][i], dp[n - 1][i + 1] - dungeon[n - 1][i])

        # last column
        for i in range(n - 2, -1, -1):
            dp[i][m - 1] = max(dp[i][m - 1], dp[i + 1][m - 1] - dungeon[i][m - 1])

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                dp1 = max(dp[i][j], dp[i + 1][j] - dungeon[i][j])
                dp2 = max(dp[i][j], dp[i][j + 1] - dungeon[i][j])
                dp[i][j] = min(dp1, dp2)

        print(dp)
        return dp[0][0]
