"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(start, size, tmp):
            if size == k:
                res.append(tmp[:])
                return

            for i in range(start, n - (k - size) + 2):
                # cut branch to improve speed
                tmp.append(i)
                backtracking(i + 1, size + 1, tmp)
                tmp.pop()

        nums = [i for i in range(1, n + 1)]
        res = []

        backtracking(1, 0, [])
        return res
