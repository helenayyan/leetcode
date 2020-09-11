"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curr_candidates, path, curr_target):
            if curr_target == 0:
                res.append(path[:])
                return

            for i, candidate in enumerate(curr_candidates):
                if candidate > curr_target or (i > 0 and candidate == curr_candidates[i - 1]):
                    # cut branch and remove duplicate
                    continue

                path.append(candidate)
                dfs(curr_candidates[i + 1:], path, curr_target - candidate)
                path.pop()

        candidates.sort()
        dfs(candidates, [], target)

        return res
