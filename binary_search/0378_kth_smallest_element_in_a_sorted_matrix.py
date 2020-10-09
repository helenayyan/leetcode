"""

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13
"""
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            # checking started from bottom left corner
            i = n - 1  # row
            j = 0  # column
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


"""
    Second method: two stack: slower than the first one
"""


class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res_stack = []
        sub_stack = []
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if not res_stack:
                    res_stack.append(matrix[i][j])
                else:
                    while sub_stack:
                        if sub_stack[-1] >= matrix[i][j]:
                            break
                        res_stack.append(sub_stack.pop())

                    while res_stack[-1] > matrix[i][j]:
                        sub_stack.append(res_stack.pop())
                    res_stack.append(matrix[i][j])

        return res_stack[k - 1]
