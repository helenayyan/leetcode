"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []

"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        if n < 4:
            return res

        for i, num in enumerate(nums[:-3]):
            # cut branches
            if num + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if (i > 0 and num == nums[i - 1]) or num + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            # set second num and follow 3sum procedure
            for j in range(i + 1, n - 2):
                p = j + 1
                q = n - 1
                # delete duplicate
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                while p < q:
                    curr_sum = num + nums[j] + nums[p] + nums[q]
                    if curr_sum < target:
                        p += 1
                    elif curr_sum > target:
                        q -= 1
                    else:
                        res.append([num, nums[j], nums[p], nums[q]])
                        # delete duplicate
                        while p < q and nums[p + 1] == nums[p]:
                            p += 1
                        while p < q and nums[q - 1] == nums[q]:
                            q -= 1
                        p += 1
                        q -= 1

        return res
