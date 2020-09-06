from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = self.helper([-1] * n, 0, n, [])
        return res

    def helper(self, positions, rowIndex, n, res):
        if rowIndex == n:
            result = self.printSolution(positions, n)
            res.append(result)
            return

        for column in range(n):
            positions[rowIndex] = column
            if self.isValid(positions, rowIndex):
                self.helper(positions, rowIndex + 1, n, res)
        return res

    def isValid(self, positions, rowIndex):
        for i in range(rowIndex):
            if positions[i] == positions[rowIndex]:
                return False
            if abs(positions[i] - positions[rowIndex]) == rowIndex - i:
                return False
        return True

    def printSolution(self, positions, n):
        result = []
        for row in range(n):
            lines = ""
            for col in range(n):
                if positions[row] == col:
                    lines += "Q"
                else:
                    lines += "."
            result.append(lines)
        return result