from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curr_target, path):
            if curr_target == 0:
                res.append(path[:])
                return
            elif curr_target < 0:
                return

            for candidate in candidates:
                if candidate <= curr_target:
                    if path and candidate >= path[-1] or not path:
                        path.append(candidate)
                        print(curr_target, path)
                        dfs(curr_target - candidate, path)
                        path.pop()

        dfs(target, [])

        return res
