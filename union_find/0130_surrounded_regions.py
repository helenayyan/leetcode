"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""
from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # BFS Method
        if not board:
            return

        n = len(board)
        m = len(board[0])
        if n <= 2 or m <= 2:
            return

        queue = deque()

        # find all the 'o' on the boards and mark them as 'a'
        for i in range(m):
            if board[0][i] == 'O':
                board[0][i] = 'A'
                queue.append([0, i])
            if board[-1][i] == 'O':
                board[-1][i] = 'A'
                queue.append([n - 1, i])
        for i in range(n):
            if board[i][0] == 'O':
                board[i][0] = 'A'
                queue.append([i, 0])

            if board[i][-1] == 'O':
                board[i][-1] = 'A'
                queue.append([i, m - 1])

        # BFS
        while queue:
            curr_loc = queue.pop()
            row = curr_loc[0]
            col = curr_loc[1]
            direction = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

            for x, y in direction:
                if 0 <= x < n and 0 <= y < m and board[x][y] == "O":
                    board[x][y] = 'A'
                    queue.append([x, y])

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
